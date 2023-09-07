from shutil import copyfileobj
from pathlib import Path

from fastapi import UploadFile

from app.config import get_settings


def save_upload(upload: UploadFile, identifier: str):
    path = Path(get_settings().UPLOAD_DIR) / identifier
    with open(path, mode='wb') as destination:
        copyfileobj(upload.file, destination)
