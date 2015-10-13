from flask_sqlalchemy import SQLAlchemy
from interncsfsu.student import constants as STUDENT

db = SQLAlchemy()

""""
The student database model
"""
class Student(db.Model):
    __tablename__ = 'Student'
    StudentID = db.Column(db.String, primary_key=True )
    name = db.Column(db.String(STUDENT.MAX_NAME))
    gpa = db.Column(db.Float)
    interest = db.Column(db.String(STUDENT.MAX_INTEREST))
    password = db.Column(db.String(STUDENT.MAX_PASSWORD))

    def __init__(self, sid, name, gpa, interest, password):
        self.StudentID = sid
        self.name = name.title()
        self.gpa = gpa
        self.interest = interest
        self.password = password


