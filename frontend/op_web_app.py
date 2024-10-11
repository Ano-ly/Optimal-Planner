#!/usr/bin/env python3
"""Optimal Planner web app that serves the html pages"""

from flask import Flask, render_template, url_for
import json

op_web_app = Flask(__name__)

@op_web_app.route("/", strict_slashes=False)
def serve_first_page():
    """Serve landing page"""
    return(render_template("index.html"))

@op_web_app.route("/login", strict_slashes=False)
def serve_login_page():
    """Serve page for user login"""
    return(render_template("login.html"))

@op_web_app.route("/about", strict_slashes=False)
def serve_about_page():
    """Serve about page"""
    return(render_template("about.html"))

@op_web_app.route("/contact", strict_slashes=False)
def serve_contact_page():
    """Serve contact page"""
    return(render_template("contact.html"))

@op_web_app.route("/event", strict_slashes=False)
def serve_event_page():
    """Serve event page"""
    return(render_template("events.html"))

@op_web_app.route("/signup", strict_slashes=False)
def serve_signup_page():
    """Serve event page"""
    return(render_template("signup.html"))

if __name__=="__main__":
    op_web_app.run("0.0.0.0", port=5001)
