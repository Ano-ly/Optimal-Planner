#!/usr/bin/env python3

""" 
Database setup module

This module sets up a SQLite database using SQLAlchemy and creates all tables
defined in the `models.base` module.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


engine = create_engine('sqlite:///optimal_planner_db.sqlite', echo=True)

Base.metadata.bind = engine

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()
