#!/usr/bin/env python3
"""Functions that serve as interface to database"""

from typing import Dict
from models.event import Event
from engine.database import session


def create_event(obj: ):
    """Create new event"""

    if obj.get(category) == None:
        return ("Event category not provided")
    new = Event(**obj)
    session.add(new)
    return (new)
