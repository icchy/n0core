from sqlalchemy import (
    Column,
    Integer, String, DateTime, Enum,
    Text,
)

from .common import *
from .objectbase import ObjectBase


VOLUME_STATE_CLAIMED = 'claimed'
VOLUME_STATE_RELEASED = 'released'
VOLUME_STATE_DESTROYED = 'destroyed'

volume_state_type = Enum(
    VOLUME_STATE_CLAIMED, VOLUME_STATE_RELEASED, VOLUME_STATE_DESTROYED,
    name='volume_state_type'
)


class Volume(ObjectBase):
    __tablename__ = 'volume'

    state = Column(volume_state_type, nullable=False)
    volume_type = Column(String, nullable=False)
    size = Column(String, nullable=False)
    url = Column(String)
