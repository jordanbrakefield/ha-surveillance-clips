from pathlib import Path
from datetime import datetime
from typing import Optional, Union


class StorageService:
    def __init__(self, root_path: Union[str, Path]):
        self.root_path = Path(root_path).resolve()

    def list_clips(self):
        clips = []

        for file in self.root_path.rglob("*.mp4"):
            if not file.is_file():
                continue

            stat = file.stat()

            clips.append(
                {
                    "filename": file.name,
                    "relative_path": file.relative_to(self.root_path).as_posix(),
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(
                        stat.st_mtime
                    ).isoformat(),
                }
            )

        clips.sort(key=lambda clip: clip["modified"], reverse=True)

        return clips

    def get_clip(self, relative_path: str) -> Optional[Path]:
        """Return a clip only when it is an MP4 inside the configured root."""
        requested_path = Path(relative_path)
        if requested_path.is_absolute():
            return None

        clip_path = (self.root_path / requested_path).resolve()
        if self.root_path not in (clip_path, *clip_path.parents):
            return None

        if clip_path.suffix.lower() != ".mp4" or not clip_path.is_file():
            return None

        return clip_path
