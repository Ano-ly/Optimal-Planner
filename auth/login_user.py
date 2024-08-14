#!/usr/bin/env python3
""" login user"""

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
import bcrypt

def authenticate_user(db: Session, username: str, password: str):
    """Check if a user exists and if their password matches"""
    user = db.query(user.User).filter(user.User.username == username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user
    return None

def login_user(db: Session, username: str, email: str, password: str):
    """ """
    user = authenticate_user(db, username, password)
    
    try:
        if user:
            if user.email == valid_email:
                if is_valid_email(email):
                        return "Login successful!"
                else:
                    return "Invalid email format."
            else:
                    return "Email or password is incorrect."
        else:
            return "Username does not exist."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred during login."
