#!/usr/bin/env python3
"""Invite views"""

from flask import abort, jsonify
from api.v1.views import app_views
from models.invite import Invite
from engine.database import session

@app_views.route("/invite/event/<int:evnt_id>", strict_slashes=False, methods=["GET"])
def get_invite_by_event(evnt_id):
    """Get all invites in a certain event"""
    try:
        invites = [inv for inv in Invite.get_invites(session) if inv["event_id"]
== evnt_id]
    except Exception as e:
        #abort(500)
        return(jsonify(f"Error: {e}"))
    else:
        return(jsonify(invites))

@app_views.route("/invite/<int:inv_id>", strict_slashes=False, methods=["GET"])
def get_invite(inv_id):
    """Get all invites"""
    try:
        invites = Invite.get_invites(session)
        for invite in invites:
            if invite["id"] == inv_id:
                return (jsonify(invite))
        else:
            return (jsonify({}))
    except Exception as e:
        return(jsonify(f"Ev: {e}"))
        #abort(404)

@app_views.route("/invite/<int:inv_id>", strict_slashes=False,
methods=["DELETE"])
def delete_invite(inv_id):
    """Delete a invite by id"""
    try:
        Invite.delete_obj(session, inv_id)
    except Exception as e:
        return(jsonify(f"Error: {e}"))
        #abort(404)
    else:
        return (jsonify({}))

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
