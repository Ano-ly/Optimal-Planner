#!/usr/bin/env python3
"""Test get_users function"""

from models.user import User
from models.budget import Budget
from models.budget_item import BudgetItem
from models.event import Event
from models.task import Task
from models.invite import Invite
from engine.database import session

user1 = User.create_user(session, "user1", "user1_pswd", "user1@gmail.com")
user2 = User.create_user(session, "user2", "user2_pswd", "user2@gmail.com")
user3 = User.create_user(session, "user3", "user3_pswd", "user3@gmail.com")
user4 = User.create_user(session, "user4", "user4_pswd", "user4@gmail.com")
user5 = User.create_user(session, "user5", "user5_pswd", "user5@gmail.com")

for item in User.get_users(session):
    print(item)

new_event = Event.create_event(session, "Wedding", 56, user1.id)
new_event2 = Event.create_event(session, "Wedding", 76, user1.id)
new_event3 = Event.create_event(session, "Wedding", 86, user1.id)
new_event4 = Event.create_event(session, "Wedding", 96, user1.id)

for item in Event.get_events(session):
    print(item)

new_budget = Budget.create_budget(session, 40000, new_event.id)
new_budget2 = Budget.create_budget(session, 50000, new_event2.id)
new_budget3 = Budget.create_budget(session, 60000, new_event3.id)
new_budget4 = Budget.create_budget(session, 70000, new_event4.id)


for item in Budget.get_budgets(session):
    print(item)

item1 = BudgetItem.create_item(session, "New budget item 1", 6000,
new_budget.id)

item2 = BudgetItem.create_item(session, "New budget item 2", 6000,
new_budget.id)
item3 = BudgetItem.create_item(session, "New budget item 3", 6000,
new_budget.id)
for item in BudgetItem.get_items(session):
    print(item)

new_task1 = Task.create_task(session, new_event.id, "Task 1", "Do this")
new_task2 = Task.create_task(session, new_event.id, "Task 2", "Do this")
new_task3 = Task.create_task(session, new_event.id, "Task 3", "Do this")
new_task4 = Task.create_task(session, new_event.id, "Task 4", "Do this")
for item in Task.get_tasks(session):
    print(item)

new_invite1 = Invite.create_invite(session, new_event.id, "Fortune1",
"fortune1@gmail.com", "09029875637")
new_invite2 = Invite.create_invite(session, new_event.id, "Fortune2",
"fortune2@gmail.com", "09029875637")
new_invite3 = Invite.create_invite(session, new_event.id, "Fortune3",
"fortune3@gmail.com", "09029875637")
for item in Invite.get_invites(session):
    print(item)
