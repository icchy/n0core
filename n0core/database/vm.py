from sqlalchemy import (
    Column,
    Integer, String, Enum,
)

from .common import *
from .objectbase import ObjectBase


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


class VM(ObjectBase):
    __tablename__ = 'vm'

    state = Column(vm_state_type, nullable=False)
    arch = Column(String, nullable=False)
    vcpus = Column(Integer, nullable=False)
    memory = Column(String, nullable=False)
    vnc_password = Column(String, nullable=False)
