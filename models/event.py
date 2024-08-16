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
    
    def create_event(Session: Session, event_type: str,
                     location: str,
                     guest: int, 
                     description: str = None):
        """ Creates a new event"""
        new_event = Event(category=event_type, time_created=datetime.now(),
                      desc=description, location="")
        Session.add(new_event)
        Session.commit()
        return new_event
    
    def update_event(session: Session, event_id: int,
                    event_type: str = None,
                    location: str = None,
                    guest: int = None,
                    description: str = None) -> Event:
        """Update an existing event."""
        # Fetch the event by ID
        event = session.query(Event).filter_by(id=event_id).first()
        try:
            if event:
                # Update the event's type if provided
                if event_type:
                    event.category = event_type
                
                # Update the event's description if provided
                if description:
                    event.desc = description
                
                # Update the event's location if provided
                if location:
                    event.location = location
                
                # Update the number of Guest if provided
                if guest:
                    event.guest = guest
                
                # Commit the changes to the database
                session.commit()
                
                return event
        except Exception as e:
            session.rollback()
            return "An error occurred"
        else:
                return None
