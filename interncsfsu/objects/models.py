from interncsfsu.database import db
from interncsfsu.objects import constants as const


class Resume(db.Model):
    __tablename__ = 'resume'
    author = db.Column(db.Integer, db.ForeignKey('Student.ID'), primary_key=True)
    file = db.Column(db.String(const.MAX_FILE_PATH))
    student = db.relationship('Student', uselist=False, backref=db.backref('resume',uselist=False))

    def __init__(self, file):
        self.file = file


class Internship(db.Model):
    __tablename__ = 'internship'
    id = db.Column(db.Integer, primary_key=True)
    companyid = db.Column(db.Integer, db.ForeignKey('Company.id'))
    position = db.Column(db.String(const.MAX_POSITION))
    startdate = db.Column(db.DateTime)
    location = db.Column(db.String(const.MAX_LOCATION))
    applicationlink = db.Column(db.String(const.MAX_APPL_LINK))
    description = db.Column(db.String(const.MAX_DESCRIPTION))

    company = db.relationship('Company', backref='internships')

    def __init__(self, companyid, position, startdate, location, applicationlink, description):
        self.companyid = companyid
        self.position = position
        self.startdate = startdate
        self.location = location
        self.applicationlink = applicationlink
        self.description = description
