#!/usr/bin/env python3
"""Budget views"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.budget import Budget
from engine.database import session

@app_views.route("/budget/event/<int:evnt_id>", strict_slashes=False, methods=["GET"])
def get_budget_by_event(evnt_id):
    """Get all budgets under a certain event"""
    try:
        for budg in Budget.get_budgets(session):
            if budg["event_id"] == evnt_id:
                return (jsonify(budg))
        else:
            return(jsonify({}))
    except Exception as e:
        abort(404, description=f"{e}")

@app_views.route("/budget/<int:budg_id>", strict_slashes=False, methods=["GET"])
def get_budget(budg_id):
    """Get a budget by id"""
    try:
        budgets = Budget.get_budgets(session)
        for budget in budgets:
            if budget["id"] == budg_id:
                return (jsonify(budget))
        else:
            return (jsonify({}))
    except Exception as e:
        abort(404, description=f"{e}")

@app_views.route("/budget/<int:budg_id>", strict_slashes=False,
methods=["DELETE"])
def delete_budget(budg_id):
    """Delete a budget by id"""
    try:
        Budget.delete_obj(session, budg_id)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return (jsonify({}))

@app_views.route("/budget", strict_slashes=False,
methods=["POST"])
def create_budget():
    """
    Create a new budget

    Required request parameters: event_id, total
    Optional request parameters: Nil
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    if "event_id" not in req:
        abort(400, description="Event id(event_id) not included")
    if "total" not in req:
        abort(400, description="Total(total) not included")
    evnt_id = req.get("event_id")
    total = req.get("total")
    try:
        new_budget = Budget.create_budget(session, total,evnt_id)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(new_budget.id))

@app_views.route("/budget/<int:budg_id>", strict_slashes=False,
methods=["PUT"])
def update_budget(budg_id):
    """
    Update a budget based on id

    Required request parameters: Nil
    Optional request parameters: total
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    _total = req.get("total")
    try:
        upd_budget = Budget.update_budget(session, budg_id, _total)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(upd_budget.id))
