from io import BytesIO
import os
from shutil import rmtree

import pytest
from fastapi import UploadFile

from app.config import get_settings


@pytest.fixture(scope='function')
def upload():
    settings = get_settings()
    file = BytesIO(b'0x0' * 1024)
    upload_file = UploadFile(file)
    os.mkdir(settings.UPLOAD_DIR)
    yield upload_file
    rmtree(settings.UPLOAD_DIR)

