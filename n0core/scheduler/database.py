from sqlalchemy import (
    create_engine,
    Column,
    Integer, String, Boolean, DateTime, Enum,
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


class VM(Base):
    __tablename__ = 'vm'

    id = Column(String(36), nullable=False)  # uuid
    name = Column(String(255), nullable=False)

    state = Column(vm_state_type, nullable=False)
    arch = Column(String(16), nullable=False)
    vcpus = Column(Integer(), nullable=False)
    memory_mb = Column(Integer(), nullable=False)
    vnc_password = Column(Text(), nullable=True)




class Relations(Base):
    __tablename__ = 'relations'


