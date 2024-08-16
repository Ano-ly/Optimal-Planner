#!/usr/bin/env python
"""The Event class mappped to event table"""

from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List
from models.base import Base

class Event(Base):
    """Event class"""

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(40), nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    set_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    desc: Mapped[str] = mapped_column(String, nullable=True)
    location: Mapped[str] = mapped_column(String, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),
        nullable=False, default=None)
    user: Mapped["User"] = relationship(back_populates="events")

    tasks: Mapped[List["Task"]] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    budget: Mapped["Budget"] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    invitees: Mapped[List["Invitee"]] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    
    def create_event(Session: Session, event_type: str, description: str = None):
        """ Creates a new event"""
        new_event = Event(category=event_type, time_created=datetime.now(),
                      desc=description, location="")
        Session.add(new_event)
        Session.commit()
        return new_event
    
    def update_event(Session: Session, event_type_id: int, description: str = None):
        """ Updates an existing event"""
        update_event = Session.query(Event).filter_by(id = event_type_id).first()
        # if eve