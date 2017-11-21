from sqlalchemy import (
    Column,
    Integer, String,
    TypeDecorator,
)

from .common import *

from n0core.lib.proto import Object


class PbObjectType(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        return value.SerializeToString()

    def process_result_value(self, value, dialect):
        obj = Object()
        return obj.ParseFromString(value)


class Object(Base):
    __tablename__ = 'object'

    id = Column(Integer, primary_key=True, auto_increment=True)
    object_id = Column(UUID, nullable=False)
    name = Column(String)
    data = Column(PbObjectType)
