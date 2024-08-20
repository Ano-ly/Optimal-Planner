#!/usr/bin/env python3
""" Retrives event location from the database
and returns a google maps link to the location """
from models.event import Event
from sqlalchemy.orm import Session

def get_event_map(session: Session, event_id: int) -> str:
    event = session.query(Event).filter_by(id=event_id).first()
    if event and event.location:
        base_url = "https://www.google.com/maps/search/?api=1&query="
        map_link = base_url + event.location.replace(" ", "+" )
        return map_link
    else:
        raise ValueError("Location not set")
