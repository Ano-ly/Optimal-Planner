#!/usr/bin/env python3
""" database setup"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import base

engine = create_engine('sqlite:///optimal_planner.db', echo=True)

SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()