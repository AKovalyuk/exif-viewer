from sqlalchemy import Column, Integer, UUID, ForeignKey, String

from app.db.models import Base


class ExifRecord(Base):
    __tablename__ = 'exif_record'

    id = Column(
        'id',
        Integer,
        primary_key=True,
    )
    operation_id = Column(
        'operation_id',
        UUID(as_uuid=True),
        ForeignKey('operation.id'),
        nullable=False,
    )
    key = Column(
        'key',
        String,
        doc='Key of EXIF record',
        nullable=False,
    )
    value = Column(
        'value',
        String,
        doc='Value of EXIF record',
        nullable=False,
    )
