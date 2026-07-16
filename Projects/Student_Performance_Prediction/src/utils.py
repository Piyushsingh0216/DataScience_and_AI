"""General utility helpers for the Student Performance project."""

from pathlib import Path


def ensure_directory(path: Path) -> Path:
    """Create a directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def format_ratio(test_size: float) -> str:
    """Return a readable train/test split ratio."""
    train_size = 1 - test_size
    return f"{int(train_size * 100)}/{int(test_size * 100)}"
