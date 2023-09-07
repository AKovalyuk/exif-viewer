from uuid import UUID
from pathlib import Path

from PIL import Image

from app.db.connection import Session
from app.utils import extract_exif
from app.db.crud import update_operation_status, create_exif_records
from app.db.models import OperationStatus
from app.celery import celery_app


@celery_app.task()
def extract_exif_task(operation_id: UUID):
    image_path = Path(f'images/{operation_id}')
    try:
        image = Image.open(image_path)
        # load now instead lazy
        image.load()
        exif_dict = extract_exif(image)
        with Session() as session:
            create_exif_records(session, operation_id, exif_dict)
            update_operation_status(session, operation_id, OperationStatus.COMPLETE)
            session.commit()
    except:
        with Session() as session:
            update_operation_status(session, operation_id, OperationStatus.ERROR)
            session.commit()
    finally:
        # cleanup
        image_path.unlink(missing_ok=True)
