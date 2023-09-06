from typing import Literal, Optional

from pydantic import BaseModel
from uuid import UUID

from app.db.models import OperationStatus


class UploadImageResponse(BaseModel):
    operation_id: UUID


class ExifKeyValue(BaseModel):
    key: str
    value: str


class OperationError(BaseModel):
    detail: str


class OperationResultResponse(BaseModel):
    operation_id: UUID
    status: OperationStatus
    result: Optional[list[ExifKeyValue] | OperationError]
