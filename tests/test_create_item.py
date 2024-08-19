#!/usr/bin/env python3
"""Test create event function"""

from models.event import Event
from models.user import User
from engine.database import session


new_user = User.create_user(session, "Cathy", "Amarachi", "cathy@gmail.com")

my_user = session.query(User).filter_by(username="Amarachi").first()

new_event = Event.create_event(session, "Wedding", 56, my_user.id, my_user)
print(new_event)

new_budget =
