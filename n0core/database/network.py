from sqlalchemy import (
    create_engine,
    Column,
    Integer, String, DateTime, Enum,
    Text,
)

NETWORK_STATE_APPLIED = 'applied'
NETWORK_STATE_HALTED = 'halted'

network_state_type = Enum(
    NETWORK_STATE_APPLIED, NETWORK_STATE_HALTED,
    name='network_state_type'
)


class Network(Base):
    __tablename__ = 'network'

    id = Column(UUID, nullable=False)
    name = Column(Text(), nullable=False)

    state = Column(network_state_type, nullable=False)
    network_type = Column(String(16), nullable=False)
    bridge = Column(String(64), nullable=False)


class Subnet(Base):
    pass
