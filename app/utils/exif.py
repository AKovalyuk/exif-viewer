from PIL import Image, ExifTags


def extract_exif(image: Image.Image):
    exif = image.getexif()
    result = {}
    for key, value in exif.items():
        result[ExifTags.TAGS.get(key, None) or f'Unknown tag {key}'] = value
    return result
