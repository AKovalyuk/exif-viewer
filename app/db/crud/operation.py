from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.models import Operation, ExifRecord, OperationStatus


async def create_operation(session: AsyncSession, initial_status=OperationStatus.RUNNING) -> Operation:
    operation = Operation(status=initial_status)
    session.add(operation)
    await session.commit()
    return operation


async def get_operation(session: AsyncSession, operation_id: UUID) -> Operation | None:
    return await session.get(Operation, operation_id)


def create_exif_records(session: Session, operation_id: UUID, kw: dict[str, str]):
    records = []
    for key, value in kw:
        records.append(ExifRecord(operation_id=operation_id, key=key, value=value))
    session.add_all(records)


async def get_exif_records(session: AsyncSession, operation_id: UUID) -> dict:
    query = select(ExifRecord).where(ExifRecord.operation_id == operation_id)
    result = {}
    for exif_record in await session.scalars(query):
        result[exif_record.key] = exif_record.value
    return result


def update_operation_status(session: Session, operation_id: UUID, status: OperationStatus):
    operation = session.get(Operation, operation_id)
    operation.status = status
