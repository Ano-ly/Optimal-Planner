
#!/usr/bin/env python3
"""Task views"""

from flask import abort, jsonify
from api.v1.views import app_views
from models.task import Task
from engine.database import session

@app_views.route("/task/event/<int:evnt_id>", strict_slashes=False, methods=["GET"])
def get_task_by_event(evnt_id):
    """Get all tasks in a certain event"""
    try:
        tasks = [tsk for tsk in Task.get_tasks(session) if tsk["event_id"]==evnt_id]
    except Exception as e:
        #abort(500)
        return(jsonify(f"Error: {e}"))
    else:
        return (jsonify(tasks))

@app_views.route("/task/<int:tsk_id>", strict_slashes=False, methods=["GET"])
def get_task(tsk_id):
    """Get all tasks"""
    try:
        tasks = Task.get_tasks(session)
        for task in tasks:
            if task["id"] == tsk_id:
                return (jsonify(task))
        else:
            return (jsonify({}))
    except Exception as e:
        return(jsonify(f"Ev: {e}"))
        #abort(404)

@app_views.route("/task/<int:tsk_id>", strict_slashes=False,
methods=["DELETE"])
def delete_task(tsk_id):
    """Delete a task by id"""
    try:
        Task.delete_obj(session, tsk_id)
    except Exception as e:
        return(jsonify(f"Error: {e}"))
        #abort(404)
    else:
        return (jsonify({}))

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
