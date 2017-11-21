from sqlalchemy import (
    create_engine,
    Column,
    Integer, String, DateTime, Enum,
    Text, TypeDecorator,
)
from sqlalchemy.ext.declarative import declarative_base

from n0core.config import config


config['db']['uri']


