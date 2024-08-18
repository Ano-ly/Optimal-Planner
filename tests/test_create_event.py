#!/usr/bin/env python3
"""Test create event function"""

from models.event import Event
from models.user import User
from engine.database import session


new_user = User(username="Ami",
                password="Mypassword",
                email="myemal@emei.com")

session.add(new_user)
my_user = session.query(User).filter_by(username="Ami").first()

new_event = Event.create_event(session, "Wedding", 56, my_user.id, my_user)
print(new_event)


