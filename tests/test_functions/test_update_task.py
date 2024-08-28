#!/usr/bin/env python3
"""Test update_task function"""

from models.event import Event
from models.task import Task
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

new_task = Task.create_task(session, new_event.id, "Task 1", "Do this")

exists_task = session.query(Task).filter_by(id=new_task.id).one_or_none()
if exists_task:
    print("DONE")
print(new_task)

upd_task = Task.update_task(session, new_task.id, "Task 1a")

print(upd_task.name)
