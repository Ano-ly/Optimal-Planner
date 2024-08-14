#!/usr/bin/env python3
"""Budget class"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List
from models.base import Base


class Budget(Base):

    """Class Budget mapped to the budget table"""
    __tablename__ = "budget"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    total: Mapped[int] = mapped_column(nullable=False)

    budget_items: Mapped[List["BudgetItem"]] = relationship(
        back_populates="budget", cascade="all, delete-orphan")

    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"),
        nullable=False)
    event: Mapped["Event"] = relationship(back_populates="budget")
