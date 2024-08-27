#!/usr/bin/env python3
""" Testing the event_maps function"""

import pytest
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from models.event_utils import get_event_map
from models.event import Event

Base = declarative_base()

class SimpleEvent(Base):
    """A simplified version of the Event model for testing."""
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String)

@pytest.fixture
def session():
    """Creates a new SQLite in-memory database session for testing."""
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    yield db
    db.close()

def test_get_event_map(session):
    """Test generating a Google Maps link for an event with a location."""
    event = SimpleEvent(location="abc transport eliozu")
    session.add(event)
    session.commit()

    expected_url = "https://www.google.com/maps/search/?api=1&query=abc+transport+eliozu"
    assert get_event_map(session, event.id) == expected_url

def test_without_location(session):
    """Test that a ValueError is raised if the event has no location."""
    event = SimpleEvent(location=None)
    session.add(event)
    session.commit()

    with pytest.raises(ValueError):
        get_event_map(session, event.id)