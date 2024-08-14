#!/usr/bin/env python3
""" database setup"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.invitee import Invitee
from models.user import User
from models.event import Event
from models.budget import budget
from models.task import Task

engine = create_engine('sqlite:///optimal_planner_db.sqlite', echo=True)

Base.metadata.bind = engine

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()