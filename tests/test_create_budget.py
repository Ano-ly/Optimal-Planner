#!/usr/bin/env python3
"""Test create budget function"""

from models.budget import Budget
from models.event import Event
from models.user import User
from engine.database import session

"""
new_user = User(username="Amiee",
                password="Mypassword",
                email="myemal@emei.com")
"""

new_user = User.create_user(session, "Amy", "Amarachi", "Amy@gmail.com")

my_user = session.query(User).filter_by(username="Amy").first()

new_event = Event.create_event(session, "Wedding", 56, my_user.id)
print(new_event)

new_budget = Budget.create_budget(session, 40000, new_event.id)

exists_budget = session.query(Budget).filter_by(id=new_budget.id).one_or_none()
if exists_budget:
    print("DONE")
print(new_budget)
