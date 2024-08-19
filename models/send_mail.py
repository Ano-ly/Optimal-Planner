#!/usr/bin/env python3
from models.invitee import Invitee
from sqlalchemy.orm import Session
import smtplib
""" """

session = Session()

def login_gmail(email_id: str, email_id_password: str):
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

def send_mail(server, email_id: str):
    invitee_emails = session.query(Invitee.email).all()
    for dest in invitee_emails:
        message = "Message."
        try:
            server.sendmail(email_id, dest.email, message)
        except Exception as e:
            raise Exception(f"Failed to send email to {dest.email}: {e}")

    session.close()
