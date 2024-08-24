#!/usr/bin/env python3
"""Application Programming Interface"""

from flask import abort, Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from engine.database import session


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close session"""
    session.close()

@app.errorhandler(404)
def handle_error(error):
    """Handle not-found error"""
    return (jsonify({"error": f"{error}"}), 404)

@app.errorhandler(403)
def handle_error(error):
    """Handle 403 error"""
    return (jsonify({"error": "Forbidden"}), 403)

@app.errorhandler(400)
def handle_error(error):
    """Handle 400 error"""
    return (jsonify({"error": f"{error}"}), 403)

@app.errorhandler(500)
def handle_server_error(error):
    """Handle server error"""
    return (jsonify({"error": f"{error}"}), 500)

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
