from sqlalchemy import (
    Column,
    Integer, String, DateTime, Enum,
    Text,
)

from .common import *


VOLUME_STATE_CLAIMED = 'claimed'
VOLUME_STATE_RELEASED = 'released'
VOLUME_STATE_DESTROYED = 'destroyed'

volume_state_type = Enum(
    VOLUME_STATE_CLAIMED, VOLUME_STATE_RELEASED, VOLUME_STATE_DESTROYED,
    name='volume_state_type'
)


class Volume(Base):
    __tablename__ = 'volume'

    id = Column(UUID, nullable=False)
    name = Column(Text(), nullable=False)

    state = Column(volume_state_type, nullable=False)
    volume_type = Column(String(16), nullable=False)
    size_mb = Column(Integer(), nullable=False)
    url = Column(String(255), nullable=True)
