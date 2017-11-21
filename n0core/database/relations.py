from sqlalchemy import (
    Column,
    Integer, String,
)

from .common import *


class Relations(Base):
    __tablename__ = 'relations'

    id = Column(Integer, primary_key=True, auto_increment=True)
    object_id = Column(UUID, nullable=False)
    to = Column(UUID, nullable=False)
