"""Windows PATH management library."""

from .path_manager import (
    EXIT_CONFLICT_ERROR,
    EXIT_GENERAL_ERROR,
    EXIT_PERMISSION_ERROR,
    EXIT_SUCCESS,
    EXIT_VALIDATION_ERROR,
    PathManager,
    PathManagerError,
    PathUpdateConflict,
)

__all__ = [
    "PathManager",
    "PathManagerError",
    "PathUpdateConflict",
    "EXIT_SUCCESS",
    "EXIT_GENERAL_ERROR",
    "EXIT_PERMISSION_ERROR",
    "EXIT_CONFLICT_ERROR",
    "EXIT_VALIDATION_ERROR",
]

__version__ = "0.1.0"
