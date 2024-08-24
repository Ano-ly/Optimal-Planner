
#!/usr/bin/env python3
"""Event views"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User
from models.event import Event
from engine.database import session

@app_views.route("/event/user/<int:usr_id>", strict_slashes=False, methods=["GET"])
def get_event_by_user(usr_id):
    """Get all events by a certain user"""
    try:
        events = [ev for ev in Event.get_events(session) if ev["user_id"]==usr_id]
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return (jsonify(events))

@app_views.route("/event/<int:evt_id>", strict_slashes=False, methods=["GET"])
def get_event(evt_id):
    """Get event by id"""
    try:
        events = Event.get_events(session)
        for event in events:
            if event["id"] == evt_id:
                return (jsonify(event))
        else:
            return (jsonify({}))
    except Exception as e:
        abort(404, description=f"{e}")

@app_views.route("/event/<int:evt_id>", strict_slashes=False,
methods=["DELETE"])
def delete_event(evt_id):
    """Delete an event by id"""
    try:
        Event.delete_obj(session, evt_id)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return (jsonify({}))

@app_views.route("/event", strict_slashes=False,
methods=["POST"])
def create_event():
    """
    Create new event

    Required request parameters: catg, guest, userid
    Optional request parameters: loc, date, desc
    """

    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    if "catg" not in req:
        abort(400, description="Event category not included")
    if "guest" not in req:
        abort(400, description="Event guests not included")
    if "userid" not in req:
        abort(400, description="Event user_id not included")
    catg = req.get("catg")
    gst = req.get("guest")
    userid = req.get("userid")
    loc = req.get("loc")
    date = req.get("date")
    description = req.get("desc")
    try:
        new_event = Event.create_event(session, catg, gst, userid, loc, date, description)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(new_event.id))


@app_views.route("/event/<int:evnt_id>", strict_slashes=False,
methods=["PUT"])
def update_event(evnt_id):
    """
    Update an event based on id

    Required request parameters: Nil
    Optional request parameters: catg, guest, loc, date, desc
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    catg = req.get("catg")
    gst = req.get("gst")
    loc = req.get("loc")
    date = req.get("date")
    description = req.get("desc")
    try:
        upd_event = Event.update_event(session, evnt_id, catg, gst, loc, date, description)
    except Exception as e:
        return(jsonify(f"Ev: {e}"))
    else:
        return(jsonify(upd_event.id))
