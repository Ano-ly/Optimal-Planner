#!/usr/bin/env python3

""" database setup"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.user import User
from models.invitee import Invitee
from models.event import Event
from models.budget import Budget
from models.budget_item import BudgetItem
from models.task import Task

engine = create_engine('sqlite:///optimal_plannerdb.sqlite', echo=True)

Base.metadata.bind = engine

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()
