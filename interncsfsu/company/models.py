from flask_sqlalchemy import SQLAlchemy
from interncsfsu.company import constants as COMPANY

db = SQLAlchemy()

"""
The company database model
"""
class Company(db.Model):
    __tablename__ = 'Company'
    name = db.Column(db.String(COMPANY.MAX_NAME), primary_key=True)
    contact = db.Column(db.String(COMPANY.MAX_CONTACT))
    website = db.Column(db.String(COMPANY.MAX_WEBSITE))
    user = db.Column(db.String(COMPANY.MAX_USERNAME))
    password = db.Column(db.String(COMPANY.MAX_PASSWORD))

    def __init__(self, name, contact, website, user, password):
        self.name = name.title()
        self.contact = contact
        self.website = website
        self.user = user
        self.password = password