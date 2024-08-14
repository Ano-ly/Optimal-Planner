#!/usr/bin/env python
"""The Event class mappped to event table"""

from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List
from models.base import Base

class Event(Base):
    """Event class"""

    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(40), nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    set_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    desc: Mapped[str] = mapped_column(String, nullable=True)
    location: Mapped[str] = mapped_column(String, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"),
        nullable=False)
    user: Mapped["User"] = relationship(back_populates="events")

    tasks: Mapped[List["Task"]] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    budget: Mapped["Budget"] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    invitees: Mapped[List["Invitee"]] = relationship(
        back_populates="event", cascade="all, delete-orphan")
