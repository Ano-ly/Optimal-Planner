#!/usr/bin/env python3
""" User class """

import bcrypt
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from models.base import Base
from typing import List
from itsdangerous import URLSafeTimedSerializer
import smtplib


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    confirmed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    confirmed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    events: Mapped[List["Event"]] = relationship(back_populates="user")

    @classmethod
    def create_user(cls, db: Session, username: str, password: str, email: str):
        """Create a new user"""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') # hash the user password
        new_user = User(username=username, password=hashed_password, email=email)
        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            
            # Generate confirmation token
            s = URLSafeTimedSerializer(app_secret_key)
            token = s.dumps(new_user.email, salt=security_password_salt)
            
            server = login_gmail(EMAIL_ID, EMAIL_PASSWORD)
            send_confirmation_email(server, new_user.email, token)
            logout_gmail(server)
        
        except Exception as e:
            db.rollback()
            raise e
        return (new_user)
    
    def send_user_confirmation_email(user):
        token = generate_confirmation_token(user.email)
    confirm_url = url_for('confirm_email', token=token, _external=True)
    html = render_template('user_registration.html', username=user.username, confirm_url=confirm_url)
    subject = "Welcome to Optimal Planner - Confirm Your Email"
    send_email(user.email, subject, html)

