#!/usr/bin/env python3
from models.invitee import Invitee
from sqlalchemy.orm import Session
from itsdangerous import URLSafeTimedSerializer
import smtplib
""" """

session = Session()

s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

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
        
def generate_confirmation_token(email):
    return s.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    try:
        email = s.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=expiration)
    except:
        return False
    return email

    session.close()
