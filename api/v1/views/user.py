#!/usr/bin/env python3
"""User views"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User
from engine.database import session

@app_views.route("/users", strict_slashes=False, methods=["GET"])
def get_users():
    """Get all users"""
    try:
        users = User.get_users(session)
    except Exception as e:
        abort(404, description=f"{e}")
        #return(jsonify(f"Ev: {e}"))
    else:
        return(jsonify(users))

@app_views.route("/user/<int:usr_id>", strict_slashes=False, methods=["GET"])
def get_user(usr_id):
    """Get user by id"""
    try:
        users = User.get_users(session)
        for user in users:
            if user["id"] == usr_id:
                return (jsonify(user))
        else:
            return (jsonify({}))
    except Exception as e:
        abort(404, description=f"{e}")
        #return(jsonify(f"Ev: {e}"))

@app_views.route("/user/<int:usr_id>", strict_slashes=False,
methods=["DELETE"])
def delete_user(usr_id):
    """Delete a user by id"""
    try:
        User.delete_obj(session, usr_id)
    except Exception as e:
        abort(404, description=f"{e}")
        #return(jsonify(f"Ev: {e}"))
    else:
        return (jsonify({}))

@app_views.route("/user", strict_slashes=False,
methods=["POST"])
def create_user():
    """
    Create a new user

    Required request parameters: username, password, email
    Optional request parameters: Nil
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    if "username" not in req:
        abort(400, description="Username not included")
    if "password" not in req:
        abort(400, description="Password not included")
    if "email" not in req:
        abort(400, description="Email not included")
    username = req.get("username")
    password = req.get("password")
    email = req.get("email")
    try:
        new_user = User.create_user(session, username, password, email)
    except Exception as e:
        abort(404, description=f"{e}")
        #return(jsonify(f"Ev: {e}"))
    else:
        return(jsonify(new_user.id))

@app_views.route("/user/<int:usr_id>", strict_slashes=False,
methods=["PUT"])
def update_user(usr_id):
    """
    Update a user based on id

    Required request parameters: Nil
    Optional request parameters: username, password, email
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    nm = req.get("username")
    eml = req.get("email")
    pswd = req.get("password")
    try:
        upd_user = User.update_user(session, usr_id, nm, eml, pswd)
    except Exception as e:
        abort(404, description=f"{e}")
        #return(jsonify(f"Ev: {e}"))
    else:
        return(jsonify(upd_user.id))
