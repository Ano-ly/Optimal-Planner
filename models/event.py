#!/usr/bin/env python
"""The event object"""

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List
from models.base import Base

class Event(Base):
    """Event class"""

    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(40))
    time_created: Mapped[str] = mapped_column(DateTime)
    set_date: Mapped[str] = mapped_column(DateTime)
    desc: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="events")

    tasks: Mapped[List["Task"]] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    budget: Mapped["Budget"] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    invitees: Mapped[List["Invitee"]] = relationship(
        back_populates="event", cascade="all, delete-orphan")
