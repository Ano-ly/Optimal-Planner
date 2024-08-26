#!/usr/bin/env python3
"""BudgetItem views"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.budget_item import BudgetItem
from engine.database import session

@app_views.route("/budget_item/budget/<int:budg_id>", strict_slashes=False, methods=["GET"])
def get_budget_item_by_budget(budg_id):
    """Get all budget_items in a certain budget"""
    try:
        items = [item for item in BudgetItem.get_items(session) if item["budget_id"]==budg_id]
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(items))

@app_views.route("/budget_item/<int:b_id>", strict_slashes=False, methods=["GET"])
def get_budget_item(b_id):
    """Get a particular budget_item"""
    try:
        budget_items = BudgetItem.get_items(session)
        for budget_item in budget_items:
            if budget_item["id"] == b_id:
                return (jsonify(budget_item))
        else:
            return (jsonify({}))
    except Exception as e:
        abort(404, description=f"{e}")

@app_views.route("/budget_item/<int:b_id>", strict_slashes=False,
methods=["DELETE"])
def delete_budget_item(b_id):
    """Delete a budget_item by id"""
    try:
        BudgetItem.delete_obj(session, b_id)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return (jsonify({}))

@app_views.route("/budget_item", strict_slashes=False,
methods=["POST"])
def create_budget_item():
    """
    Create a new budget_item

    Required request parameters: budg_id, total, desc
    Optional request parameters: Nil
    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    if "budg_id" not in req:
        abort(400, description="Budget id(budg_id) not included")
    if "total" not in req:
        abort(400, description="Total(total) not included")
    if "desc" not in req:
        abort(400, description="Description(desc) not included")
    budg_id = req.get("budg_id")
    _total = req.get("total")
    description = req.get("desc")
    try:
        new_budget_item = BudgetItem.create_item(session, description, _total, budg_id)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(new_budget_item.id))

@app_views.route("/budget_item/<int:b_id>", strict_slashes=False,
methods=["PUT"])
def update_budget_item(b_id):
    """
    Update a budget item based on id

    Required request parameters: Nil
    Optional request parameters: desc, total

    """
    if not request.get_json():
        abort(400, description="Not a valid JSON")
    req = request.get_json()
    desc = req.get("desc")
    _total = req.get("total")
    try:
        upd_item = BudgetItem.update_item(session, b_id, desc, _total)
    except Exception as e:
        abort(404, description=f"{e}")
    else:
        return(jsonify(upd_item.id))
