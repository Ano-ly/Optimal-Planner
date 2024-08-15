#!/usr/bin/env python3
""" login user"""

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
import getpass
import bcrypt

def authenticate_user(db: Session, identify: str, password: str):
    """Check if a user exists and if their password matches"""
    if is_valid(identify):
        user = db.query(User).filter(User.username == identify).first()
    else:
        user = db.query(User).filter(User.email == identify).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user
    return None

def login_user(db: Session, identify: str, password: str):
    """ Logs user in with either Username or email """
    user = authenticate_user(db, identify, password)
    
    try:
        if user:
            return "Login successful!"
        else:
            return "Email/Username or password is incorrect."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred during login."
