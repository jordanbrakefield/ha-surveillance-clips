from pathlib import Path
from datetime import datetime


class StorageService:
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)

    def list_clips(self):
        clips = []

        for file in self.root_path.rglob("*.mp4"):
            stat = file.stat()

            clips.append(
                {
                    "filename": file.name,
                    "relative_path": str(file.relative_to(self.root_path)),
                    "full_path": str(file),
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(
                        stat.st_mtime
                    ).isoformat(),
                }
            )

        clips.sort(key=lambda clip: clip["modified"], reverse=True)

        return clips