from itsdangerous import URLSafeSerializer
from flask_mail import Message

from interncsfsu import app, mail
from config import ADMINS as admins

ts = URLSafeSerializer(app.config['SECRET_KEY'])


def send_email(subject, html_body, sender=admins[0], recipients=admins[0]):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    mail.send(msg)