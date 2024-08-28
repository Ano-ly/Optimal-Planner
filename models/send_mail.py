#!/usr/bin/env python3
""" 
Email Sender Module
=====================
This module provides functions to send emails to guests of an event using a Gmail account.
It uses SQLAlchemy to interact with the database and retrieve guest email addresses."""


from models.invite import Invite
from sqlalchemy.orm import Session
import smtplib


session = Session()

def login_gmail(email_id: str, email_id_password: str) -> smtplib.SMTP:
    """
    This function logs into a Gmail account using SMTP protocol.

    Parameters:
    email_id (str): The email address of the Gmail account.
    email_id_password (str): The password of the Gmail account.

    Returns:
    smtplib.SMTP: An SMTP server object if login is successful.

    Raises:
    Exception: If login fails, an exception is raised with a descriptive error message.
    """
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_id, email_id_password)
        return server
    except Exception as e:
        raise Exception(f"Failed to login: {e}")


def logout_gmail(server):
    try:
        server.quit()
        return("Logout successful")
    except Exception as e:
        return(f"Failed to logout: {e}")

def send_mail(server, email_id: str, event_id: int, session: Session):
    """
    This function sends an email to all guests of an event using an SMTP server.

    Parameters:
    server (smtplib.SMTP): An SMTP server object that is already logged in.
    email_id (str): The email address of the sender.

    Returns:
    None

    Raises:
    Exception: If an error occurs while sending an email to a guest, an exception is raised with a descriptive error message.
    """
    invitee_emails = session.query(Invite.email).filter_by(event_id=event_id).all()
    for dest in invitee_emails:
        message = "Message."
        try:
            server.sendmail(email_id, dest.email, message)
        except Exception as e:
            raise Exception(f"Failed to send email to {dest.email}: {e}")

    session.close()
