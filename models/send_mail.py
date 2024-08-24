#!/usr/bin/env python3
from models.invitee import Invitee
from sqlalchemy.orm import Session
from itsdangerous import URLSafeTimedSerializer
from utils import mail_config
import smtplib

class Mail_utils:
    def __init__(self, secret_key, security_password_salt):
        self.serializer = URLSafeTimedSerializer(secret_key)
        self.security_password_salt = security_password_salt

    def login_gmail(self, email_id: str, email_id_password: str):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_id, email_id_password)
            return server
        except Exception as e:
            raise Exception(f"Failed to login: {e}")

    def logout_gmail(self, server):
        try:
            server.quit()
            return "Logout successful"
        except Exception as e:
            return f"Failed to logout: {e}"

    def send_mail(self, server, email_id: str):
        session = Session()
        invitee_emails = session.query(Invitee.email).all()
        for dest in invitee_emails:
            message = "Message."
            try:
                server.sendmail(email_id, dest.email, message)
            except Exception as e:
                raise Exception(f"Failed to send email to {dest.email}: {e}")
            finally:
                session.close()

    def generate_confirmation_token(self, email: str):
        return self.serializer.dumps(email, salt=self.security_password_salt)

    def send_user_confirmation_email(self, user):
        token = self.generate_confirmation_token(user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('user_registration.html', username=user.username, confirm_url=confirm_url)
        subject = "Welcome to Optimal Planner - Confirm Your Email"
        send_email(user.email, subject, html)

    def confirm_token(self, token: str, expiration: int = 3600):
        try:
            email = self.serializer.loads(token, salt=self.security_password_salt, max_age=expiration)
        except:
            return False
        return email

    def send_guest_confirmation_mail(self, event, guest):
        token = self.generate_confirmation_token(guest.email)
        confirm_url = url_for('confirm_guest', event_id=event.id, token=token, _external=True)
        html = render_template('guest_registration.html', event_name=event.name, confirm_url=confirm_url)
        subject = f"Welcome to {event.name} - Confirm Your Email"
        send_email(guest.email, subject, html)
