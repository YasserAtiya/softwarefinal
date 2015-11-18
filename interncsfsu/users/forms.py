from flask_wtf import Form
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField, PasswordField, TextAreaField ,validators, DateField
from wtforms_components import If
from config import ALLOWED_EXTENSIONS as extensions
from interncsfsu.users.constants import MAX_MSG as max_msg

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
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match' )])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])
    #add a Captcha field

class StudentSettingsForm(Form):
    first_name = StringField('First Name', validators=[validators.Optional()])
    last_name = StringField('Last Name', validators=[validators.Optional()])
    resume = FileField('Resume', validators=[validators.Optional(), FileAllowed(extensions, ', '.join(extensions))])
    about = TextAreaField('About', validators=[validators.Optional(), validators.Length(max=max_msg)])

class CompanySettingsForm(Form):
    name = StringField('Company Name', validators=[validators.Optional()])
    website = StringField('Website', validators=[validators.Optional(), validators.Regexp('^[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU)$', message='Valid URL Required')])
    contact = StringField('Contact Email', validators=[validators.Optional(), validators.Email()])
    new_password = PasswordField('New Password', validators=[validators.Optional(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', validators=[If( lambda form, field: form.new_password.data,
                                                                validators.DataRequired())])

class InternshipForm(Form):
    position = StringField('Position', validators=[validators.DataRequired()])
    startdate = StringField('Start Date', validators=[validators.DataRequired()])
    location = StringField('Location', validators=[validators.DataRequired()])
    applicationlink = StringField('Application Link', validators=[validators.Optional()])
    description = StringField('Description', validators=[validators.DataRequired()])
