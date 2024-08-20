#!/usr/bin/env python3
"""Test create_item function for creating new budget items"""

from engine.database import session
from models.budget import Budget
from models.budget_item import BudgetItem
from models.event import Event
from models.user import User


new_user = User.create_user(session, "Cam", "Amarachi", "cam@gmail.com")

my_user = session.query(User).filter_by(username="Cam").first()

new_event = Event.create_event(session, "Wedding", 56, my_user.id)
print(new_event)

new_budget = Budget(total=5000, event_id=new_event.id, event=new_event)
session.add(new_budget)
session.commit()
print("\n\n\n")
print(new_budget.total)

new_item = BudgetItem.create_item(session, "New budget item 1", 6000,
new_budget.id)
print(new_item, new_item.total)
if type(new_item) != str:
    print(new_item.desc, new_item.total)
else:
    print(str)
