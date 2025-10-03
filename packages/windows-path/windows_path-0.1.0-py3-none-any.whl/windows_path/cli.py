"""Command line interface for the windows_path package."""

import argparse
import sys
import traceback
from typing import Iterable, List, Optional

from .path_manager import (
    EXIT_CONFLICT_ERROR,
    EXIT_GENERAL_ERROR,
    EXIT_SUCCESS,
    EXIT_VALIDATION_ERROR,
    PathManager,
    PathManagerError,
    PathUpdateConflict,
)


def build_parser() -> argparse.ArgumentParser:
    description = "Windows PATH Manager - Manage the user PATH environment variable"
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    windows_path list
    windows_path add "C:\\Python39\\Scripts"
    windows_path add --position start "C:\\MyTools"
    windows_path remove "C:\\OldPath"
    windows_path clean --force
    windows_path deduplicate
    windows_path search python
    windows_path backup
    windows_path restore path_backup_20250103.json
    windows_path export csv > paths.csv
        """,
    )

    parser.add_argument("command", help="Command to execute")
    parser.add_argument("args", nargs="*", help="Command arguments")
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Skip confirmations (for automation)",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Quiet mode",
    )
    parser.add_argument(
        "--position",
        "-p",
        default="end",
        help="Position for add command (start/end/number)",
    )

    return parser


def _ensure_windows() -> None:
    if sys.platform != "win32":
        raise PathManagerError(
            "Error: This tool only works on Windows.", EXIT_GENERAL_ERROR
        )


def _dispatch(manager: PathManager, command: str, arguments: Iterable[str], position: str) -> None:
    args_list = list(arguments)

    if command == "list":
        manager.list_paths()
    elif command == "add":
        if not args_list:
            raise PathManagerError("Error: 'add' command requires a path argument.", EXIT_VALIDATION_ERROR)
        manager.add_path(args_list[0], position=position)
    elif command == "remove":
        if not args_list:
            raise PathManagerError(
                "Error: 'remove' command requires a path argument.", EXIT_VALIDATION_ERROR
            )
        manager.remove_path(args_list[0])
    elif command == "clean":
        manager.clean_paths()
    elif command == "deduplicate":
        manager.deduplicate_paths()
    elif command == "search":
        if not args_list:
            raise PathManagerError(
                "Error: 'search' command requires a query argument.", EXIT_VALIDATION_ERROR
            )
        manager.search_paths(args_list[0])
    elif command == "backup":
        filename = args_list[0] if args_list else None
        manager.backup_path(filename)
    elif command == "restore":
        if not args_list:
            raise PathManagerError(
                "Error: 'restore' command requires a filename argument.", EXIT_VALIDATION_ERROR
            )
        manager.restore_path(args_list[0])
    elif command == "export":
        format_type = args_list[0] if args_list else "txt"
        manager.export_paths(format_type)
    else:
        raise PathManagerError(f"Error: Unknown command '{command}'", EXIT_VALIDATION_ERROR)


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        _ensure_windows()
    except PathManagerError as exc:
        print(str(exc), file=sys.stderr)
        return exc.exit_code

    manager = PathManager(verbose=args.verbose, quiet=args.quiet, force=args.force)
    command = args.command.lower()

    try:
        _dispatch(manager, command, args.args, args.position)
        return EXIT_SUCCESS
    except PathManagerError as exc:
        # Error already logged by PathManager._error
        return exc.exit_code
    except PathUpdateConflict:
        print("Error: PATH changed concurrently. Please retry.", file=sys.stderr)
        return EXIT_CONFLICT_ERROR
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        return EXIT_GENERAL_ERROR
    except Exception as exc:  # pragma: no cover - unforeseen errors
        print(f"Unexpected error: {exc}", file=sys.stderr)
        if args.verbose:
            traceback.print_exc()
        return EXIT_GENERAL_ERROR


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
