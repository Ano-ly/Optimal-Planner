#!/usr/bin/env python3
"""Task class for event tasks"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base

class Task(Base):
   """Task Class"""

   __tablename__ = "tasks"

   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str] = mapped_column(String)
   desc: Mapped[str] = mapped_column(String)

   event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
   event: Mapped["Event"] = relationship(back_populates="tasks")
