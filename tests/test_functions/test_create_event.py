#!/usr/bin/env python3
"""Test create event function"""

from models.event import Event
from models.user import User
from engine.database import session

"""
new_user = User(username="Amiee",
                password="Mypassword",
                email="myemal@emei.com")
"""

new_user = User.create_user(session, "Amiee", "Amarachi", "Amie@gmail.com")

my_user = session.query(User).filter_by(username="Amiee").first()

new_event = Event.create_event(session, "Wedding", 56, my_user.id)
print(new_event)
