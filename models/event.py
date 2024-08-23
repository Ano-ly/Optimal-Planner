#!/usr/bin/env python
"""The Event class mappped to event table"""

from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session
from typing import List
from models.base import Base
from models.user import User

class Event(Base):
    """Event class"""

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(40), nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    set_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=True)
    desc: Mapped[str] = mapped_column(String, nullable=True)
    location: Mapped[str] = mapped_column(String, nullable=True)
    guest: Mapped[int] = mapped_column(Integer, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),
        nullable=False, default=None)
    user: Mapped["User"] = relationship(back_populates="events")

    tasks: Mapped[List["Task"]] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    budget: Mapped["Budget"] = relationship(
        back_populates="event", cascade="all, delete-orphan")
    invites: Mapped[List["Invite"]] = relationship(
        back_populates="event", cascade="all, delete-orphan")

    @classmethod
    def create_event(cls, session: Session,
                     catg: str,
                     gst: int,
                     userid: str,
                     loc: str = None,
                     date: datetime = None,
                     description: str = None) -> "Event":
        """ Creates a new event"""
        _user = session.query(User).filter_by(id=userid).one()
        if _user:
            try:

                new_event = Event(category=catg, guest=gst, user_id=userid,
                                  user=_user, desc=description, location=loc,
                                  set_date=date)
                session.add(new_event)
                session.commit()
                return (new_event)
            except Exception as e:
                session.rollback()
                raise Exception(f"An Error occured: {e}")
        else:
            raise Exception("User not found")


    @classmethod
    def update_event(self, session: Session,
                     event_id: int,
                     catg: str,
                     guest: int,
                     loc: str = None,
                     date: datetime = None,
                     description: str = None) -> "Event":
        """Update an existing event."""
        # Fetch the event by ID
        event = session.query(Event).filter_by(id=event_id).one_or_none()
        if event:
            try:
                # Update the event's type if provided
                if catg:
                    event.category = catg
                # Update the event's description if provided
                if description:
                    event.desc = description
                # Update the event's location if provided
                if loc:
                    event.location = loc
                # Update the number of Guest if provided
                if guest:
                    event.guest = guest
                # Update the date for event to hold if provided
                if date:
                    event.set_date = date

                # Commit the changes to the database
                session.commit()

                return (event)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Item not found")

