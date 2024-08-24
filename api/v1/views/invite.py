#!/usr/bin/env python3
"""Invite views"""

from flask import abort, jsonify, request
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
        abort(404, description=f"{e}")
    else:
        return(jsonify(invites))

@app_views.route("/invite/<int:inv_id>", strict_slashes=False, methods=["GET"])
def get_invite(inv_id):
    """Get invite by id"""
    try:
        invites = Invite.get_invites(session)
        for invite in invites:
            if invite["id"] == inv_id:
                return (jsonify(invite))
        else:
            return (jsonify({}))
    except Exception as e:
        abort(404, description=f"{e}")

@app_views.route("/invite/<int:inv_id>", strict_slashes=False,
methods=["DELETE"])
def delete_invite(inv_id):
    """Delete a invite by id"""
    try:
        Invite.delete_obj(session, inv_id)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return (jsonify({}))

@app_views.route("/invite", strict_slashes=False,
methods=["POST"])
def create_invite():
    """
    Create a new invite

    Required request parameters: event_id, name
    Optional request parameters: email, phone_no
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    if "event_id" not in req:
        abort(400, description="Event id(event_id) not included")
    if "name" not in req:
        abort(400, description="Name not included")
    nm = req.get("name")
    evnt_id = req.get("event_id")
    eml = req.get("email")
    ph_no = req.get("phone_no")
    try:
        new_invite = Invite.create_invite(session, evnt_id, nm, eml, ph_no)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(new_invite.id))

@app_views.route("/invite/<int:inv_id>", strict_slashes=False,
methods=["PUT"])
def update_invite(inv_id):
    """
    Update an invite based on id

    Required request parameters: Nil
    Optional request parameters: name, email, phone_no
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    nm = req.get("name")
    eml = req.get("email")
    ph_no = req.get("phone_no")
    try:
        upd_invite = Invite.update_invite(session, inv_id, nm, eml, ph_no)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(upd_invite.id))
