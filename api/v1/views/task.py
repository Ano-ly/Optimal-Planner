
#!/usr/bin/env python3
"""Task views"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.task import Task
from engine.database import session

@app_views.route("/task/event/<int:evnt_id>", strict_slashes=False, methods=["GET"])
def get_task_by_event(evnt_id):
    """Get all tasks in a certain event"""
    try:
        tasks = [tsk for tsk in Task.get_tasks(session) if tsk["event_id"]==evnt_id]
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return (jsonify(tasks))

@app_views.route("/task/<int:tsk_id>", strict_slashes=False, methods=["GET"])
def get_task(tsk_id):
    """Get task by id"""
    try:
        tasks = Task.get_tasks(session)
        for task in tasks:
            if task["id"] == tsk_id:
                return (jsonify(task))
        else:
            return (jsonify({}))
    except Exception as e:
        abort(404, description=f"{e}")

@app_views.route("/task/<int:tsk_id>", strict_slashes=False,
methods=["DELETE"])
def delete_task(tsk_id):
    """Delete a task by id"""
    try:
        Task.delete_obj(session, tsk_id)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return (jsonify({}))

@app_views.route("/task", strict_slashes=False,
methods=["POST"])
def create_task():
    """
    Create a new task

    Required request parameters: event_id, name
    Optional request parameters: desc
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    if "event_id" not in req:
        abort(400, description="Event id(event_id) not included")
    if "name" not in req:
        abort(400, description="Name(name) not included")
    event_id = req.get("event_id")
    nm = req.get("name")
    desc = req.get("desc")
    try:
        new_task = Task.create_task(session, evnt_id, nm, desc)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(new_task.id))

@app_views.route("/task/<int:tsk_id>", strict_slashes=False,
methods=["PUT"])
def update_task(tsk_id):
    """
    Update a task based on id

    Required request parameters: Nil
    Optional request parameters: name, desc
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    nm = req.get("name")
    dsc = req.get("desc")
    try:
        upd_task = Task.update_task(session, tsk_id, nm, dsc)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(upd_task.id))
