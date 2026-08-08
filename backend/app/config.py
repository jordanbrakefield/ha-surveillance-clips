"""Application configuration read from the environment."""

import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def get_clips_path() -> Path:
    """Return the configured directory containing surveillance clips.

    The directory must be supplied explicitly so the application works in
    containers and never relies on a developer-specific filesystem path.
    """
    value = os.getenv("CLIPS_PATH")
    if not value:
        raise RuntimeError(
            "CLIPS_PATH must be set to the directory containing surveillance clips."
        )

    path = Path(value).expanduser()
    if not path.is_dir():
        raise RuntimeError(f"CLIPS_PATH is not an existing directory: {path}")

    return path.resolve()
