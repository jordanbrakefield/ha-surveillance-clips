# ha-surveillance-clips
Home Assistant integration for managing and viewing self-hosted surveillance clips

## Backend development

Set `CLIPS_PATH` in `backend/.env` to a directory containing your video clips.
Copy `backend/.env.example` when setting up another machine. The real `.env` file
is intentionally ignored by Git.

Then start the API:

```sh
source backend/.venv/bin/activate
uvicorn app.main:app --app-dir backend --reload
```

For containers, mount the clips directory at `/clips` and set `CLIPS_PATH=/clips`.
