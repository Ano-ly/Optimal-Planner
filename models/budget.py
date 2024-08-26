#!/usr/bin/env python3
"""Budget class"""

from copy import deepcopy
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
        if evnt.budget is not None:
            raise Exception("Budget already exists")
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
    def get_budgets(cls, session):
        """Get all budget items"""
        try:
            b_items = session.query(cls).all()
        except Exception as e:
            raise Exception (f"An error occurred: {e}")
        else:
            dict_b = [deepcopy(b.__dict__) for b in b_items]
            for dic in dict_b:
                del(dic["_sa_instance_state"])
            return (dict_b)
