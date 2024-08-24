#!/usr/bin/env python3
"""User views"""

from flask import abort, jsonify
from api.v1.views import app_views
from models.user import User
from engine.database import session

@app_views.route("/users", strict_slashes=False, methods=["GET"])
def get_users():
    """Get all users"""
    try:
        users = User.get_users(session)
    except Exception as e:
        #abort(500)
        return(jsonify(f"Error: {e}"))
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
        return(jsonify(f"Ev: {e}"))
        #abort(404)

@app_views.route("/user/<int:usr_id>", strict_slashes=False,
methods=["DELETE"])
def delete_user(usr_id):
    """Delete a user by id"""
    try:
        User.delete_obj(session, usr_id)
    except Exception as e:
        return(jsonify(f"Error: {e}"))
        #abort(404)
    else:
        return (jsonify({}))

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
