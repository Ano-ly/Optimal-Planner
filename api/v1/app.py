#!/usr/bin/env python3
"""Application Programming Interface"""

from flask import Flask

app = Flask(__name__)

@app.route("api/v1/events/<user_id>", strict_slashes=False, methods=["GET"])
def get_events(user_id):

