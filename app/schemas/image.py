from typing import Literal, Optional

from pydantic import BaseModel
from uuid import UUID


class UploadImageResponse(BaseModel):
    operation_id: UUID


class ExifKeyValue(BaseModel):
    key: str
    value: str


class OperationError(BaseModel):
    detail: str


class OperationResultResponse(BaseModel):
    operation_id: UUID
    status: Literal["running", "error", "complete"]
    result: Optional[list[ExifKeyValue] | OperationError]
