#!/usr/bin/env python3
"""Budget views"""

from flask import abort, jsonify
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

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
