#!/usr/bin/env python3
"""Invitee class for event invitees"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base

class Invitee(Base):
   """Invitee Class"""

   __tablename__ = "invitees"

   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str] = mapped_column(String(100))
   email: Mapped[str] = mapped_column(String(100))
   phone_no: Mapped[str] = mapped_column(String(100))

   event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
   event: Mapped["Event"] = relationship(back_populates="invitees")
