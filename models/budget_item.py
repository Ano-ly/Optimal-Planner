#!/usr/bin/env python3
"""BudgetItem class"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session
from models.base import Base
from models.budget import Budget


class BudgetItem(Base):

    """Class Budget mapped to the budget table"""
    __tablename__ = "budgetitems"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    desc: Mapped[str] = mapped_column(String, nullable=False)
    total: Mapped[int] = mapped_column(nullable=False)

    budget_id: Mapped[int] = mapped_column(ForeignKey("budgets.id"),
        nullable=False)
    budget: Mapped["Budget"] = relationship(back_populates="budget_items")


    @classmethod
    def create_item(cls,
                    session: Session,
                    description: str,
                    _total: int,
                    budg_id: int) -> "BudgetItem":
        """Create budget item attached to budget"""
        budg = session.query(Budget).filter_by(id=budg_id).one_or_none()
        if budg:
            try:
                new_item = BudgetItem(desc=description,
                                      total=_total,
                                      budget_id=budg_id,
                                      budget=budg)
                session.add(new_item)
                session.commit()
                return (new_item)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Item not found")

    @classmethod
    def update_item(cls,
                    session: Session,
                    item_id: int,
                    description: str = None,
                    _total: int = None) -> "BudgetItem":
        """Update budget item information"""
        item = session.query(cls).filter_by(id=item_id).one_or_none()
        if item:
            try:
                if description:
                    item.desc = description
                if _total:
                    item.total = _total
                session.add(item)
                session.commit()
                return (item)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Item not found")

