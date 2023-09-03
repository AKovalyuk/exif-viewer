from uuid import UUID

from fastapi import APIRouter, UploadFile, status

from app.schemas import UploadImageResponse, OperationResultResponse


router = APIRouter(prefix='/image')


@router.post(
    '',
    response_model=UploadImageResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload(file: UploadFile):
    """
    Upload image to extract EXIF
    """
    pass


@router.get(
    '/{operation_id}',
    response_model=OperationResultResponse,
    status_code=status.HTTP_200_OK,
)
async def get_operation_result(operation_id: UUID):
    """
    Get operation result
    """
    pass
