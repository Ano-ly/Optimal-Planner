#!/usr/bin/env python3
"""BudgetItem class"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.base import Base


class BudgetItem(Base):

    """Class Budget mapped to the budget table"""
    __tablename__ = "budgetitem"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    desc: Mapped[str] = mapped_column(String, nullable=False)
    total: Mapped[int] = mapped_column(nullable=False)

    budget_id: Mapped[int] = mapped_column(ForeignKey("budget.id"),
        nullable=False)
    budget: Mapped["Budget"] = relationship(back_populates="budget_items")
