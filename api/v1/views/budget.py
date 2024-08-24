#!/usr/bin/env python3
"""Budget views"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.budget import Budget
from engine.database import session

@app_views.route("/budget/event/<int:evnt_id>", strict_slashes=False, methods=["GET"])
def get_budget_by_event(evnt_id):
    """Get all budgets in a certain event"""
    try:
        for budg in Budget.get_budgets(session):
            if budg["event_id"] == evnt_id:
                return (jsonify(budg))
        else:
            return(jsonify({}))
    except Exception as e:
        #abort(500)
        return(jsonify(f"Error: {e}"))

@app_views.route("/budget/<int:budg_id>", strict_slashes=False, methods=["GET"])
def get_budget(budg_id):
    """Get all budgets"""
    try:
        budgets = Budget.get_budgets(session)
        for budget in budgets:
            if budget["id"] == budg_id:
                return (jsonify(budget))
        else:
            return (jsonify({}))
    except Exception as e:
        return(jsonify(f"Ev: {e}"))
        #abort(404)

@app_views.route("/budget/<int:budg_id>", strict_slashes=False,
methods=["DELETE"])
def delete_budget(budg_id):
    """Delete a budget by id"""
    try:
        Budget.delete_obj(session, budg_id)
    except Exception as e:
        return(jsonify(f"Error: {e}"))
        #abort(404)
    else:
        return (jsonify({}))

@app_views.route("/budget", strict_slashes=False,
methods=["POST"])
def create_budget():
    """Create a new budget"""
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    if "evnt_id" not in req:
        abort(400, description="Event id(evnt_id) not included")
    if "_total" not in req:
        abort(400, description="Total(_total) not included")
    evnt_id = req.get("evnt_id")
    _total = req.get("_total")
    try:
        new_budget = Budget.create_budget(session, _total,evnt_id)
    except Exception as e:
        return(jsonify(f"Ev: {e}"))
        #abort(404, description=f"{e}")
    else:
        return(jsonify(new_budget.id))

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
