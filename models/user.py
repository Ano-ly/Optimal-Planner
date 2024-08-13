#!/usr/bin/env python3
""" User class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True);
    username: Mapped[str] = mapped_column(String(200), unique=True, nullable=False);
    password: Mapped[str] = mapped_column(String(255), nullable=False);
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False);
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow);
    update_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onUpdate=datetime.utcnow);