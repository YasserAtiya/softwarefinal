from flask_wtf import Form
from wtforms import StringField, PasswordField, FloatField, validators
from interncsfsu.student import models


class StudentRegisterForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired()])
    gpa =  FloatField('GPA')
    interest = StringField('Interest')


class StudentLoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email() ])
    password = PasswordField('Password', [validators.DataRequired()])

