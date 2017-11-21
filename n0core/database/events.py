from sqlalchemy import (
    Column,
    Integer, Bool, String, DateTime, Enum,
)

from .common import *


EVENT_SCHEDULED = 'scheduled'
EVENT_APPLIED = 'applied'

event_type = Enum(
    EVENT_SCHEDULED, EVENT_APPLIED,
    name='event_type'
)


class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, auto_increment=True)
    spec = Column(UUID, nullable=False)
    object = Column(UUID, nullable=False)
    created_at = Column(DateTime)
    event = Column(event_type, default=EVENT_SCHEDULED)
    succeeded = Column(Bool, nullable=False)
    msg = Column(String)
