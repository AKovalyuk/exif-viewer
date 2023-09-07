from io import BytesIO

from PIL import Image
import pytest


@pytest.fixture
def png_image():
    img = Image.new('RGB', (100, 100))
    with BytesIO() as out:
        img.save(out, format='PNG')
        return out.getvalue()


@pytest.fixture
def jpeg_with_exif():
    img = Image.new('RGB', (100, 100))
    sample_exif = Image.Exif()
    sample_exif[1] = 'InteropIndex'
    with BytesIO() as out:
        img.save(out, format='JPEG', exif=sample_exif)
        return out.getvalue()


@pytest.fixture
def jpeg_without_exif():
    img = Image.new('RGB', (100, 100))
    with BytesIO() as out:
        img.save(out, format='JPEG')
        return out.getvalue()
