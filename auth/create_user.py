#!/usr/bin/env python3
from sqlalchemy.orm import Session
from models import user
import bcrypt
""" manage user authentication """

# def authenticate_user(db: Session, username: str, password: str):
#     """Check if a user exists and if their password matches"""
#     user = db.query(user.User).filter(user.User.username == username).first()
#     if user and user.password == password:
#         return user
#     return None

def create_user(db: Session, username: str, password: str, email: str):
    """Create a new user"""
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = user.User(username=username, password=hashed_password, email=email)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise e
    return new_user
