#!/usr/bin/env python3
"""Test create event function"""

from models.event import Event
from models.invite import Invite
from models.user import User
from engine.database import session

"""
new_user = User(username="Amiee",
                password="Mypassword",
                email="myemal@emei.com")
"""

new_user = User.create_user(session, "Amyy", "Amarachi", "Amyy@gmail.com")

my_user = session.query(User).filter_by(username="Amyy").first()

new_event = Event.create_event(session, "Wedding", 56, my_user.id)
print(new_event)

new_invite = Invite.create_invite(session, new_event.id, "Fortune",
"fortune@gmail.com", "09029875637")

exists_invite = session.query(Invite).filter_by(id=new_invite.id).one_or_none()
if exists_invite:
    print("DONE")
print(new_invite)

upd_invite = Invite.update_invite(session, new_invite.id, "Fort")

print(upd_invite.name)
