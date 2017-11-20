from sqlalchemy import (
    String
)
from sqlalchemy.ext.declarative import declarative_base


UUID = String(36)  # uuid length
Base = declarative_base()


__all__ = ['Base', 'UUID']
