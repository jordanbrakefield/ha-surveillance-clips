from pathlib import Path


class StorageService:

    def __init__(self, root_path):
        self.root_path = Path(root_path)


    def list_clips(self):
        return list(self.root_path.rglob("*.mp4"))