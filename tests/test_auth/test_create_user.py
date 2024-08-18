#!/usr/bin/env python3
"""Test file for create_user function"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.user import User
from auth.create_user import create_user

# Setup for the in-memory database
@pytest.fixture
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    yield db
    db.close()

def test_create_user(test_db):
    # Test creating a new user
    new_user = create_user(test_db, "testuser", "testpassword", "test@example.com")

    # Verify the user was created
    assert new_user.username == "testuser"
    assert new_user.email == "test@example.com"
    assert new_user.id is not None

    # Verify that the password was hashed
    assert new_user.password != "testpassword"  # Password should be hashed, so it shouldn't match the plain password

test_create_user(test_db())
