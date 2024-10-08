#!/usr/bin/env python3
"""Task class for event tasks"""

from copy import deepcopy
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session
from models.base import Base
from models.event import Event

class Task(Base):
    """Task Class"""

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    desc: Mapped[str] = mapped_column(String, nullable=True)

    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    event: Mapped["Event"] = relationship(back_populates="tasks")

    @classmethod
    def create_task(cls,
                    session: Session,
                    evnt_id: int,
                    nm: str,
                    desc: str = None) -> "Task":
        """Create a new task"""
        evnt = session.query(Event).filter_by(id=evnt_id).one_or_none()
        if evnt:
            try:
                new_task = Task(event_id=evnt_id, event=evnt, name=nm, desc=desc)
                session.add(new_task)
                session.commit()
                return (new_task)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Event not found")


    @classmethod
    def update_task(cls,
                      session: Session,
                      task_id: int,
                      nm: str = None,
                      dsc: str = None) -> "Invite":
        """Update task information"""
        tsk = session.query(cls).filter_by(id=task_id).one_or_none()
        if tsk:
            try:
                if nm:
                    tsk.name = nm
                if dsc:
                    tsk.desc = dsc
                session.add(tsk)
                session.commit()
                return (tsk)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Item not found")

    @classmethod
    def get_tasks(cls, session):
        """Get all tasks"""
        try:
            tasks = session.query(cls).all()
        except Exception as e:
            raise Exception (f"An error occurred: {e}")
        else:
            dict_tasks = [deepcopy(tsk.__dict__) for tsk in tasks]
            for dic in dict_tasks:
                del(dic["_sa_instance_state"])
            return (dict_tasks)
