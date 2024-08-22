#!/usr/bin/env python3
"""Base object; declarative base"""

from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    """Base class"""

    pass
