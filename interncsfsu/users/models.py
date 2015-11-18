from interncsfsu.database import db
from interncsfsu.users import constants as const

'''
The generic User type
'''


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(const.MAX_STRING))
    password = db.Column(db.String(const.MAX_STRING))
    role = db.Column(db.String(const.MAX_STRING))
    authenticated = db.Column(db.Integer)
    student = db.relationship('Student', uselist=False, backref='user')
    company = db.relationship('Company', uselist=False, backref='user')

    is_authenticated = True
    is_active = True
    is_anonymous = False

    def __init__(self, email, password, role, authenticated, active=True, anonymous=False):
        self.email = email
        self.password = password
        self.role = role
        self.authenticated = authenticated
        self.is_authenticated = self.authenticated
        self.is_active = active
        self.is_anonymous = anonymous

    def __repr__(self):
        return '<User ID %r , User Email %r, User Role: %r >' % (self.id, self.email, self.role)

    def get_id(self):
        return str(self.id)


'''
Model for Student information table
'''


class Student(db.Model):
    __tablename__ = 'Student'
    ID = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    FName = db.Column(db.String(const.MAX_STRING))
    LName = db.Column(db.String(const.MAX_STRING))
    PreviousLogin = db.Column(db.Integer)
    Year = db.Column(db.String(const.MAX_YEAR))
    GradDate = db.Column(db.DateTime)
    About = db.Column(db.String(const.MAX_MSG))

    def __repr__(self):
        return '<Student ID %r , Student Name %r %r>' % (self.ID, self.FName, self.LName)

    def get_id(self):
        return str(self.id)


class Company(db.Model):
    __tablename__ = 'Company'
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    name = db.Column(db.String(const.MAX_STRING))
    website = db.Column(db.String(const.MAX_WEBSITE))
    about = db.Column(db.String(const.MAX_MSG))

    def __init__(self, id, name, website, about=''):
        self.id = id
        self.name = name
        self.website = website
        self.about = about

    def __repr__(self):
        return '<Company ID %r , Company Name %r >' % (self.id, self.name)

    def get_id(self):
        return str(self.id)
