from sqlalchemy import (
    create_engine,
    Column,
    Integer, String, DateTime, Enum,
    Text,
)

from .common import *
from .objectbase import ObjectBase


NETWORK_STATE_APPLIED = 'applied'
NETWORK_STATE_HALTED = 'halted'

network_state_type = Enum(
    NETWORK_STATE_APPLIED, NETWORK_STATE_HALTED,
    name='network_state_type'
)


class Network(ObjectBase):
    __tablename__ = 'network'

    state = Column(network_state_type, nullable=False)
    network_type = Column(String, nullable=False)
    bridge = Column(String, nullable=False)


class Subnet(Base):
    __tablename__ = 'subnet'

    id = Column(Integer(), primary_key=True)
    pass
