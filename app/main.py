from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

_STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
_INDEX_HTML = _STATIC_DIR / "index.html"


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(_INDEX_HTML)
