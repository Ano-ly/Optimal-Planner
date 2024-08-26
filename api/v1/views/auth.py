
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
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    if "username" not in req and "email" not in req:
        abort(400, description="Username not included")
    if "password" not in req:
        abort(400, description="Password not included")
    pswd = req.get("password")
    identify = req.get("username")
    if identify is None:
        identify = req.get("email")
    user = authenticate_user(session, identify, pswd)
    if user is None:
        abort(403, description="Invalid user credentials")
    else:
        return(jsonify(user.id))
