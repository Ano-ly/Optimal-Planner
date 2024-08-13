#!/usr/bin/env python3
""" User class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True);
    username = Column(String(200), unique=True, nullable=False);
    password = Column(String(255), nullable=False);
    email = Column(String(255), unique=True, nullable=False);
    created_at = Column(DateTime, default=datetime.utcnow);
    update_at = Column(DateTime, default=datetime.utcnow, onUpdate=datetime.utcnow);
    