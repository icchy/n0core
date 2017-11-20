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


config['db']['uri']


class Relations(Base):
    __tablename__ = 'relations'
