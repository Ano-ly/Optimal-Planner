#!/usr/bin/env python3
"""Budget class"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session
from typing import List
from models.base import Base
from models.event import Event


class Budget(Base):

    """Class Budget mapped to the budget table"""
    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    total: Mapped[int] = mapped_column(nullable=False)

    budget_items: Mapped[List["BudgetItem"]] = relationship(
        back_populates="budget", cascade="all, delete-orphan")

    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"),
        nullable=False)
    event: Mapped["Event"] = relationship(back_populates="budget")

    @classmethod
    def create_budget(cls,
                    session: Session,
                    _total: int,
                    evnt_id: int) -> "Budget":
        """Create budget attached to event"""
        evnt = session.query(Event).filter_by(id=evnt_id).one_or_none()
        if evnt:
            try:
                new_budget = Budget(total=_total,
                                    event_id=evnt_id,
                                    event=evnt)
                session.add(new_budget)
                session.commit()
                return (new_budget)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Item not found")

    @classmethod
    def update_budget(cls,
                    session: Session,
                    budg_id: int,
                    _total: int = None) -> "Budget":
        """Update budget information"""
        budg = session.query(cls).filter_by(id=budg_id).one_or_none()
        if budg:
            try:
                if _total:
                    budg.total = _total
                session.add(budg)
                session.commit()
                return (budg)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Item not found")

    @classmethod
    def delete_obj(cls, session: Session, obj_id: int) -> None:
        """Delete an object from the database"""

        try:
            obj = session.query(cls).filter_by(id=obj_id).one_or_none()
            if not obj:
                raise Exception("Item does not exist")
            session.delete(obj)
            session.commit()
            return (None)
        except Exception as e:
            session.rollback()
            raise Exception(f"An error occured: {e}")
