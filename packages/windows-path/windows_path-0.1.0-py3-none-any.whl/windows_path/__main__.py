"""Module entry point for ``python -m windows_path``."""

from .cli import main


def run() -> None:
    raise SystemExit(main())


if __name__ == "__main__":  # pragma: no cover
    run()
