from io import BytesIO
from pathlib import Path

from PIL import Image

from app.utils import extract_exif, save_upload
from app.config import get_settings


def test_extract_exif_wrong_format(png_image):
    img = Image.open(BytesIO(png_image))
    result = extract_exif(img)
    assert result == {}


def test_extract_exif_no_kw(jpeg_without_exif):
    img = Image.open(BytesIO(jpeg_without_exif))
    result = extract_exif(img)
    assert result == {}


def test_extract_exif(jpeg_with_exif):
    img = Image.open(BytesIO(jpeg_with_exif))
    result = extract_exif(img)
    assert result == {'InteropIndex': 'InteropIndex'}


def test_upload(upload):
    save_upload(upload, '123')
    assert (Path(get_settings().UPLOAD_DIR) / '123').exists()

