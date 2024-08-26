#!/usr/bin/env python3
"""Base object; declarative base"""

from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    """Base class"""

    @classmethod
    def delete_obj(cls, session: Session, obj_id: int) -> None:
        """Delete an object from the database"""

        try:
            obj = session.query(cls).filter_by(id=obj_id).one_or_none()
            if not obj:
                raise Exception("Item does not exist")
            session.delete(obj)
            session.commit()
            return (None)
        except Exception as e:
            session.rollback()
            raise Exception(f"An error occured: {e}")
