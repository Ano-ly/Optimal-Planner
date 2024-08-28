#!/usr/bin/env python3
"""Test update_event function"""

from models.event import Event
from models.user import User
from engine.database import session


new_user = User.create_user(session, "Ami", "Amarachi", "Ami@gmail.com")
my_user = session.query(User).filter_by(username="Ami").first()


new_event = Event.create_event(session, "Birthday", 56, my_user.id)
print(new_event.category)
upd_event = Event.update_event(session, new_event.id, "Naming Ceremony", 56)
print(upd_event.category)
