from uuid import UUID

from fastapi import APIRouter, UploadFile, status, Depends, HTTPException

from app.schemas import UploadImageResponse, OperationResultResponse, ExifKeyValue
from app.db.crud import get_operation, get_exif_records, create_operation
from app.db.connection import get_session
from app.tasks import extract_exif_task
from app.db.models import OperationStatus
from app.utils import save_upload


router = APIRouter(prefix='/image')


@router.post(
    '',
    response_model=UploadImageResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload(
        file: UploadFile,
        session=Depends(get_session),
):
    """
    Upload image to extract EXIF
    """
    new_operation = await create_operation(session)
    save_upload(file, str(new_operation.id))
    extract_exif_task.delay(new_operation.id)
    return UploadImageResponse(
        operation_id=new_operation.id,
    )


@router.get(
    '/{operation_id}',
    response_model=OperationResultResponse,
    status_code=status.HTTP_200_OK,
)
async def get_operation_result(
        operation_id: UUID,
        session=Depends(get_session),
):
    """
    Get operation result
    """
    operation = await get_operation(session, operation_id)
    if operation is None:
        raise HTTPException(status_code=404)
    exif_records_response = None
    if operation.status == OperationStatus.COMPLETE:
        exif_records = await get_exif_records(session, operation_id)
        exif_records_response = [
            ExifKeyValue(key=key, value=value) for key, value in exif_records.items()
        ]
    return OperationResultResponse(
        operation_id=operation_id,
        status=operation.status,
        result=exif_records_response,
    )
