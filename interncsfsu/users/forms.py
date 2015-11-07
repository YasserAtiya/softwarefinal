from flask_wtf import Form
from wtforms import StringField, PasswordField, validators

class StudentLoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Regexp('\w+@cs.fsu.edu', message='CS Email required' ) ])
    password = PasswordField('Password', [validators.DataRequired()])

class CompanyLoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email() ])
    password = PasswordField('Password', [validators.DataRequired()])

class CompanyApplication(Form):
    company_name = StringField('Company Name', [validators.DataRequired()])
    company_website = StringField('Company Website')
    contact = StringField('Contact Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])