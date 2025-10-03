"""Core functionality for managing the Windows user PATH variable."""

import json
import os
import sys
import winreg
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Set, Tuple, Union

EXIT_SUCCESS = 0
EXIT_GENERAL_ERROR = 1
EXIT_PERMISSION_ERROR = 2
EXIT_CONFLICT_ERROR = 3
EXIT_VALIDATION_ERROR = 4


class PathManagerError(Exception):
    """Base error for PATH manager failures."""

    def __init__(self, message: str, exit_code: int = EXIT_GENERAL_ERROR) -> None:
        super().__init__(message)
        self.exit_code = exit_code


class PathUpdateConflict(Exception):
    """Raised when PATH is modified concurrently during an update."""


class PathManager:
    """Manages the Windows user PATH environment variable."""

    def __init__(self, verbose: bool = False, quiet: bool = False, force: bool = False) -> None:
        """Initialize the PATH manager."""

        self.reg_path = r"Environment"
        self.reg_key = "PATH"
        self.verbose = verbose
        self.quiet = quiet
        self.force = force

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _error(self, message: str, exit_code: int = EXIT_GENERAL_ERROR) -> None:
        """Log an error message and raise a PathManagerError."""

        self._log(message, "error")
        raise PathManagerError(message, exit_code)

    def _log(self, message: str, level: str = "info") -> None:
        """Log messages based on verbosity settings."""

        if self.quiet and level in ("info", "debug"):
            return
        if level == "debug" and not self.verbose:
            return

        if level == "error":
            print(message, file=sys.stderr)
        else:
            print(message)

    def _open_registry(self, access: int):
        """Open the registry key for user environment variables."""

        try:
            return winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.reg_path, 0, access)
        except FileNotFoundError:
            if access & winreg.KEY_WRITE:
                return winreg.CreateKeyEx(
                    winreg.HKEY_CURRENT_USER,
                    self.reg_path,
                    0,
                    access,
                )
            raise

    def _expand_path(self, path_str: str) -> str:
        """Expand environment variables and user directory markers."""

        expanded = os.path.expandvars(path_str)
        return os.path.expanduser(expanded)

    def _sanitize_new_path(self, path_str: str) -> str:
        """Prepare a user-supplied path for storage."""

        candidate = path_str.strip().strip('"')
        if not candidate:
            return candidate
        if "%" in candidate:
            return candidate
        expanded = os.path.expanduser(candidate)
        absolute = os.path.abspath(expanded)
        return os.path.normpath(absolute)

    def _validate_path(self, path_str: Optional[str]) -> Optional[str]:
        """Validate a path string before use."""

        if not path_str:
            return "Path cannot be empty."
        if any(char in path_str for char in (";", "\n", "\r")):
            return "Path cannot contain ';' or newline characters."
        if "\x00" in path_str:
            return "Path cannot contain null characters."
        if len(path_str) > 4096:
            return "Path length exceeds 4096 characters."
        return None

    def _normalize_for_compare(self, path_str: str) -> str:
        """Normalize a path string into a case-insensitive comparable value."""

        expanded = self._expand_path(path_str.strip().strip('"'))
        try:
            normalized = str(Path(expanded).resolve(strict=False))
        except Exception:
            normalized = os.path.normpath(expanded)
        return os.path.normcase(normalized)

    def _split_path_value(self, path_value: Optional[str]) -> List[str]:
        """Split a PATH string into individual components."""

        if not path_value:
            return []
        return [segment.strip() for segment in path_value.split(';') if segment.strip()]

    def _read_current_path_state(self) -> Tuple[str, List[str]]:
        """Read and return both PATH raw value and list representation."""

        current_value = self._get_current_path()
        return current_value, self._split_path_value(current_value)

    def _is_interactive(self) -> bool:
        """Determine if the session is interactive."""

        if self.force:
            return False
        try:
            return sys.stdin is not None and sys.stdin.isatty()
        except Exception:
            return False

    def _get_current_path(self) -> str:
        """Get the current user PATH value from the registry."""

        try:
            with self._open_registry(winreg.KEY_READ) as key:
                path_value, _ = winreg.QueryValueEx(key, self.reg_key)
                return path_value
        except FileNotFoundError:
            return ""
        except Exception as exc:
            self._error(f"Error reading PATH: {exc}")

    def _set_path(self, new_path: str, expected: Optional[str] = None) -> None:
        """Set the user PATH value in the registry."""

        try:
            with self._open_registry(winreg.KEY_READ | winreg.KEY_WRITE) as key:
                try:
                    current_value, _ = winreg.QueryValueEx(key, self.reg_key)
                except FileNotFoundError:
                    current_value = ""

                if expected is not None and current_value != expected:
                    raise PathUpdateConflict()

                winreg.SetValueEx(
                    key,
                    self.reg_key,
                    0,
                    winreg.REG_EXPAND_SZ,
                    new_path,
                )
            self._broadcast_change()
        except PathUpdateConflict:
            raise
        except PermissionError:
            self._error(
                "Error: Permission denied. Try running as administrator.",
                EXIT_PERMISSION_ERROR,
            )
        except Exception as exc:
            self._error(f"Error writing PATH: {exc}")

    def _broadcast_change(self) -> None:
        """Notify Windows that environment variables have changed."""

        try:
            import ctypes

            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x001A
            SMTO_ABORTIFHUNG = 0x0002

            result = ctypes.c_long()
            SendMessageTimeout = ctypes.windll.user32.SendMessageTimeoutW
            SendMessageTimeout(
                HWND_BROADCAST,
                WM_SETTINGCHANGE,
                0,
                "Environment",
                SMTO_ABORTIFHUNG,
                5000,
                ctypes.byref(result),
            )
            self._log("Environment change broadcast sent", "debug")
        except Exception as exc:
            self._log(
                f"Warning: Could not broadcast environment change: {exc}", "debug"
            )

    def _get_path_list(self) -> List[str]:
        """Get current PATH as a list of paths."""

        _, paths = self._read_current_path_state()
        return paths

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def list_paths(self) -> None:
        """List all paths in the user PATH."""

        paths = self._get_path_list()

        if not paths:
            self._log("User PATH is empty.")
            return

        self._log(f"User PATH contains {len(paths)} entries:")
        self._log("-" * 80)
        for i, path in enumerate(paths, 1):
            expanded = self._expand_path(path)
            exists = os.path.exists(expanded)
            status = "✓" if exists else "✗"
            if expanded != path:
                self._log(f"{i:3}. [{status}] {path} (expands to: {expanded})")
            else:
                self._log(f"{i:3}. [{status}] {path}")

        self._log("-" * 80)
        self._log("✓ = Path exists | ✗ = Path not found")

    def add_path(self, new_path: str, position: Union[str, int] = "end") -> None:
        """Add a path to the user PATH."""

        user_supplied = new_path.strip().strip('"')
        cleaned_path = self._sanitize_new_path(new_path)
        validation_error = self._validate_path(cleaned_path)
        if validation_error:
            self._error(f"Error: {validation_error}", EXIT_VALIDATION_ERROR)

        normalized_new = self._normalize_for_compare(cleaned_path)
        expanded_path = self._expand_path(cleaned_path)

        exists = os.path.exists(expanded_path)
        if not exists:
            warning = f"Warning: Path does not exist: {cleaned_path}"
            if not self._is_interactive():
                self._log(warning, "error")
                if not self.force:
                    self._error(
                        "Error: Non-interactive session cannot confirm addition.",
                        EXIT_VALIDATION_ERROR,
                    )
            else:
                self._log(warning, "warning")
                response = input("Add anyway? (y/n): ").strip().lower()
                if response != "y":
                    self._log("Operation cancelled.")
                    return
        elif not os.path.isdir(expanded_path):
            self._log(
                f"Notice: Path points to a file rather than a directory: {cleaned_path}",
                "warning",
            )

        for attempt in range(3):
            current_value, paths = self._read_current_path_state()

            for existing_path in paths:
                if (
                    self._normalize_for_compare(existing_path) == normalized_new
                    or existing_path.strip().strip('"').lower() == user_supplied.lower()
                ):
                    self._log(f"Path already exists in PATH: {existing_path}")
                    return

            if position == "start":
                new_paths = [cleaned_path] + paths
            elif position == "end":
                new_paths = paths + [cleaned_path]
            else:
                try:
                    pos = int(position)
                    if pos < 0 or pos > len(paths):
                        self._error(
                            f"Error: Invalid position {pos}. Must be between 0 and {len(paths)}",
                            EXIT_VALIDATION_ERROR,
                        )
                    new_paths = paths[:pos] + [cleaned_path] + paths[pos:]
                except ValueError:
                    self._error(
                        f"Error: Invalid position '{position}'. Use 'start', 'end', or a number.",
                        EXIT_VALIDATION_ERROR,
                    )

            try:
                self._set_path(';'.join(new_paths), expected=current_value)
                self._log(f"✓ Successfully added to PATH: {cleaned_path}")
                self._log(
                    "Note: You may need to restart applications for changes to take effect."
                )
                return
            except PathUpdateConflict:
                if attempt < 2:
                    self._log("PATH changed by another process, retrying...", "debug")
                continue

        self._error(
            "Error: PATH changed concurrently. Please retry.", EXIT_CONFLICT_ERROR
        )

    def remove_path(self, path_to_remove: str) -> None:
        """Remove a path from the user PATH."""

        user_supplied = path_to_remove.strip().strip('"')
        cleaned_remove = self._sanitize_new_path(path_to_remove)
        normalized_remove = self._normalize_for_compare(cleaned_remove)

        for attempt in range(3):
            current_value, paths = self._read_current_path_state()
            new_paths: List[str] = []
            removed_paths: List[str] = []

            for existing_path in paths:
                if (
                    self._normalize_for_compare(existing_path) == normalized_remove
                    or existing_path.strip().strip('"').lower() == user_supplied.lower()
                ):
                    removed_paths.append(existing_path)
                else:
                    new_paths.append(existing_path)

            if not removed_paths:
                self._log(f"Path not found in PATH: {path_to_remove}")
                return

            try:
                self._set_path(';'.join(new_paths), expected=current_value)
                self._log(
                    f"✓ Successfully removed {len(removed_paths)} entry(ies) from PATH:"
                )
                for removed in removed_paths:
                    self._log(f"  - {removed}")
                self._log(
                    "Note: You may need to restart applications for changes to take effect."
                )
                return
            except PathUpdateConflict:
                if attempt < 2:
                    self._log("PATH changed by another process, retrying...", "debug")
                continue

        self._error(
            "Error: PATH changed concurrently. Please retry.", EXIT_CONFLICT_ERROR
        )

    def clean_paths(self) -> None:
        """Remove all non-existent paths from the user PATH."""

        for attempt in range(3):
            current_value, paths = self._read_current_path_state()
            valid_paths: List[str] = []
            removed_paths: List[str] = []

            for path in paths:
                expanded = self._expand_path(path)
                if os.path.exists(expanded):
                    valid_paths.append(path)
                else:
                    removed_paths.append(path)

            if not removed_paths:
                self._log("No invalid paths found. PATH is clean.")
                return

            self._log(f"Found {len(removed_paths)} invalid path(s):")
            for removed in removed_paths:
                self._log(f"  - {removed}")

            if self._is_interactive():
                response = input("Remove these paths? (y/n): ").strip().lower()
                if response != "y":
                    self._log("Operation cancelled.")
                    return

            try:
                self._set_path(';'.join(valid_paths), expected=current_value)
                self._log(f"✓ Cleaned {len(removed_paths)} invalid path(s) from PATH")
                return
            except PathUpdateConflict:
                if attempt < 2:
                    self._log("PATH changed by another process, retrying...", "debug")
                continue

        self._error(
            "Error: PATH changed concurrently. Please retry.", EXIT_CONFLICT_ERROR
        )

    def deduplicate_paths(self) -> None:
        """Remove duplicate paths from the user PATH."""

        for attempt in range(3):
            current_value, paths = self._read_current_path_state()
            seen: Set[str] = set()
            unique_paths: List[str] = []
            duplicates: List[str] = []

            for path in paths:
                normalized = self._normalize_for_compare(path)
                if normalized not in seen:
                    seen.add(normalized)
                    unique_paths.append(path)
                else:
                    duplicates.append(path)

            if not duplicates:
                self._log("No duplicates found. PATH is already unique.")
                return

            self._log(f"Found {len(duplicates)} duplicate(s):")
            for dup in duplicates:
                self._log(f"  - {dup}")

            if self._is_interactive():
                response = input("Remove duplicates? (y/n): ").strip().lower()
                if response != "y":
                    self._log("Operation cancelled.")
                    return

            try:
                self._set_path(';'.join(unique_paths), expected=current_value)
                self._log(f"✓ Removed {len(duplicates)} duplicate(s) from PATH")
                return
            except PathUpdateConflict:
                if attempt < 2:
                    self._log("PATH changed by another process, retrying...", "debug")
                continue

        self._error(
            "Error: PATH changed concurrently. Please retry.", EXIT_CONFLICT_ERROR
        )

    def search_paths(self, query: str) -> None:
        """Search for paths containing a specific substring."""

        paths = self._get_path_list()
        query_lower = query.lower()
        matches: List[Tuple[int, str]] = []

        for i, path in enumerate(paths, 1):
            if query_lower in path.lower():
                matches.append((i, path))

        if not matches:
            self._log(f"No paths found matching: {query}")
            return

        self._log(f"Found {len(matches)} matching path(s):")
        for idx, path in matches:
            expanded = self._expand_path(path)
            exists = os.path.exists(expanded)
            status = "✓" if exists else "✗"
            self._log(f"{idx:3}. [{status}] {path}")

    def backup_path(self, filename: Optional[str] = None) -> None:
        """Backup the current PATH to a JSON file."""

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"path_backup_{timestamp}.json"

        current_value, paths = self._read_current_path_state()
        backup_data = {
            "timestamp": datetime.now().isoformat(),
            "raw_value": current_value,
            "paths": paths,
            "count": len(paths),
        }

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(backup_data, file, indent=2)
        except Exception as exc:
            self._error(f"Error creating backup: {exc}")
        else:
            self._log(f"✓ PATH backed up to: {filename}")
            self._log(f"  Contains {len(paths)} path(s)")

    def restore_path(self, filename: str) -> None:
        """Restore PATH from a backup file."""

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                backup_data = json.load(file)
        except FileNotFoundError:
            self._error(f"Error: Backup file not found: {filename}")
        except json.JSONDecodeError:
            self._error(f"Error: Invalid backup file format: {filename}")
        except Exception as exc:
            self._error(f"Error restoring backup: {exc}")
            return
        else:
            raw_value = backup_data.get('raw_value', '')
            paths = backup_data.get('paths', [])
            timestamp = backup_data.get('timestamp', 'unknown')
            count = backup_data.get('count', len(paths))

            self._log("Backup information:")
            self._log(f"  Timestamp: {timestamp}")
            self._log(f"  Contains: {count} path(s)")

            if self._is_interactive():
                response = input("Restore this backup? (y/n): ").strip().lower()
                if response != 'y':
                    self._log("Operation cancelled.")
                    return

            self._set_path(raw_value)
            self._log("✓ PATH restored successfully")
            self._log(
                "Note: You may need to restart applications for changes to take effect."
            )

    def export_paths(self, format: str = 'txt') -> None:
        """Export PATH entries in a readable format."""

        paths = self._get_path_list()

        if format == 'txt':
            for path in paths:
                print(path)
        elif format == 'csv':
            print("Index,Path,Exists,Expanded")
            for i, path in enumerate(paths, 1):
                expanded = self._expand_path(path)
                exists = os.path.exists(expanded)
                path_escaped = path.replace('"', '""')
                expanded_escaped = expanded.replace('"', '""')
                print(f'{i},"{path_escaped}",{exists},"{expanded_escaped}")')
        elif format == 'markdown':
            print("# User PATH Entries\n")
            print(f"Total: {len(paths)} entries\n")
            print("| # | Status | Path |")
            print("|---|--------|------|")
            for i, path in enumerate(paths, 1):
                expanded = self._expand_path(path)
                exists = os.path.exists(expanded)
                status = "✓" if exists else "✗"
                path_display = path.replace('|', '\\|')
                print(f"| {i} | {status} | `{path_display}` |")
        else:
            self._error(
                f"Error: Unknown export format '{format}'", EXIT_VALIDATION_ERROR
            )
