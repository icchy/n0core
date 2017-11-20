from sqlalchemy import (
    create_engine,
    Column,
    Integer, String, DateTime, Enum,
    Text, TypeDecorator,
)
from sqlalchemy.ext.declarative import declarative_base

try:
    from n0core.config import config
except:
    import sys
    sys.path.append('../../')
    from n0core.config import config


Base = declarative_base()

config['db']['uri']


VM_STATE_STARTED = 'started'
VM_STATE_STOPPED = 'stopped'
VM_STATE_RESTARTED = 'restarted'
VM_STATE_HALTED = 'halted'
VM_STATE_DESTROYED = 'destroyed'

vm_state_type = Enum(
    VM_STATE_STARTED, VM_STATE_STOPPED, VM_STATE_RESTARTED, 
    VM_STATE_HALTED, VM_STATE_DESTROYED,
    name='vm_state_type'
)


VOLUME_STATE_CLAIMED = 'claimed'
VOLUME_STATE_RELEASED = 'released'
VOLUME_STATE_DESTROYED = 'destroyed'

volume_state_type = Enum(
    VOLUME_STATE_CLAIMED, VOLUME_STATE_RELEASED, VOLUME_STATE_DESTROYED,
    name='volume_state_type'
)


NETWORK_STATE_APPLIED = 'applied'
NETWORK_STATE_HALTED = 'halted'

network_state_type = Enum(
    NETWORK_STATE_APPLIED, NETWORK_STATE_HALTED,
    name='network_state_type'
)


UUID = String(36)  # uuid length

class VM(Base):
    __tablename__ = 'vm'

    id = Column(UUID, nullable=False)
    name = Column(Text(), nullable=False)

    state = Column(vm_state_type, nullable=False)
    arch = Column(String(16), nullable=False)
    vcpus = Column(Integer(), nullable=False)
    memory_mb = Column(Integer(), nullable=False)
    vnc_password = Column(Text(), nullable=True)


class Volume(Base):
    __tablename__ = 'volume'

    id = Column(UUID, nullable=False)
    name = Column(Text(), nullable=False)

    state = Column(volume_state_type, nullable=False)
    volume_type = Column(String(16), nullable=False)
    size_mb = Column(Integer(), nullable=False)
    url = Column(String(255), nullable=True)


class Network(Base):
    __tablename__ = 'network'

    id = Column(UUID, nullable=False)
    name = Column(Text(), nullable=False)

    state = Column(network_state_type, nullable=False)
    network_type = Column(String(16), nullable=False)
    bridge = Column(String(64), nullable=False)


class Subnet(Base):
    pass



class Relations(Base):
    __tablename__ = 'relations'


