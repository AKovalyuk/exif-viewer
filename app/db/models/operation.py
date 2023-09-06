import enum

from sqlalchemy import Column, Enum, UUID, func

from app.db.models import Base


class OperationStatus(enum.Enum):
    ERROR = 'ERROR'
    RUNNING = 'RUNNING'
    COMPLETE = 'COMPLETE'


class Operation(Base):
    __tablename__ = 'operation'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )
    status = Column(
        'status',
        Enum(OperationStatus),
        doc='Status of operation',
        nullable=False,
    )
