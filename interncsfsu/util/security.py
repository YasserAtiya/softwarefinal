from itsdangerous import URLSafeSerializer
from flask_mail import Message

from interncsfsu import app, mail
from config import ADMINS as admins

ts = URLSafeSerializer(app.config['SECRET_KEY'])


def send_email(subject,  html_body, recipients=admins):
    print(admins[0])
    msg = Message(subject, sender=admins[0], recipients=recipients)
    msg.html = html_body
    mail.send(msg)