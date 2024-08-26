#!/usr/bin/env python3
"""Invite class for event invites"""

from copy import deepcopy
from datetime import datetime
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session
from models.base import Base
from models.event import Event

class Invite(Base):
    """Invite Class"""

    __tablename__ = "invites"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    phone_no: Mapped[str] = mapped_column(String(100), nullable=True)

    confirmed: Mapped[bool] = mapped_column(Boolean, default=False)
    confirmation_token: Mapped[datetime] = mapped_column(String, nullable=True)

    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    event: Mapped["Event"] = relationship(back_populates="invites")

    @classmethod
    def create_invite(cls,
                       session: Session,
                       evnt_id: int,
                       nm: str,
                       eml: str = None,
                       ph_no: str = None) -> "Invite":
        """Create a new invite"""
        evnt = session.query(Event).filter_by(id=evnt_id).one_or_none()
        if evnt:
            try:
                new_invite = Invite(event_id=evnt_id, event=evnt, name=nm, email=eml, phone_no=ph_no)
                session.add(new_invite)
                session.commit()
                return (new_invite)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Event not found")


    @classmethod
    def update_invite(cls,
                      session: Session,
                      invite_id: int,
                      nm: str = None,
                      eml: str = None,
                      ph_no: str = None) -> "Invite":
        """Update invite information"""
        invt = session.query(cls).filter_by(id=invite_id).one_or_none()
        if invt:
            try:
                if eml:
                    invt.email = eml
                if nm:
                    invt.name = nm
                if ph_no:
                    invt.phone_no = ph_no
                session.add(invt)
                session.commit()
                return (invt)
            except Exception as e:
                session.rollback()
                raise Exception(f"An error occurred: {e}")
        else:
            raise Exception("Item not found")

    @classmethod
    def get_invites(cls, session):
        """Get all invites"""
        try:
            invites = session.query(cls).all()
        except Exception as e:
            raise Exception (f"An error occurred: {e}")
        else:
            dict_invs = [deepcopy(inv.__dict__) for inv in invites]
            for dic in dict_invs:
                del(dic["_sa_instance_state"])
            return (dict_invs)
