#!/usr/bin/env python3
"""Auth views"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from auth.login_user import authenticate_user
from models.user import User
from engine.database import session

@app_views.route("/auth", strict_slashes=False, methods=["POST"])
def auth_user():
    """
    Authenticate user

    Required request parameters: username, password
    """
    user = request.form
    user_info = {}
    for key, val in user.items():
        user_info.update({key: val})
    if "username" not in user_info:
        abort(400, description="Username not included")
    if "password" not in user_info:
        abort(400, description="Password not included")
    pswd = user_info.get("password")
    identify = user_info.get("username")
    user = authenticate_user(session, identify, pswd)
    if user is None:
        abort(403, description="Invalid user credentials")
    else:
        print(user.id)
        return(jsonify(user.id))
