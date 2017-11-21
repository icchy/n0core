from sqlalchemy import (
    Column,
    Integer, String,
)

from .common import *


class ObjectBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, auto_increment=True)
    object_id = Column(UUID, nullable=False)
    name = Column(String)
