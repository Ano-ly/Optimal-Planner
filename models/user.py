#!/usr/bin/env python3
""" User class """

import bcrypt
import copy
from typing import List
from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from models.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    events: Mapped[List["Event"]] = relationship(back_populates="user")

    @classmethod
    def create_user(cls,
                    session: Session,
                    username: str,
                    password: str,
                    email: str) -> "User":
        """Create a new user"""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(username=username, password=hashed_password, email=email)
        try:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        except Exception as e:
            session.rollback()
            raise e
        return (new_user)

    @classmethod
    def update_user(cls,
                      session: Session,
                      user_id: int,
                      usr_nm: str = None,
                      eml: str = None,
                      pswd: str = None) -> "User":
        """Update user information"""
        usr = session.query(cls).filter_by(id=user_id).one_or_none()
        if usr:
            try:
                if eml:
                    usr.email = eml
                if usr_nm:
                    usr.username = usr_nm
                if pswd:
                    hashed_password = bcrypt.hashpw(pswd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    usr.password = hashed_password
                session.add(usr)
                session.commit()
                return (usr)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("User not found")

    @classmethod
    def get_users(cls, session):
        """Get all users"""
        try:
            users = session.query(cls).all()
        except Exception as e:
            raise Exception (f"An error occurred: {e}")
        else:
            dict_users = [copy.deepcopy(user.__dict__) for user in users]
            for dic in dict_users:
                del(dic["_sa_instance_state"])
            return (dict_users)
