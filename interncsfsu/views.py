from flask import (Blueprint, flash, render_template, redirect, url_for, request)
from flask_login import login_user, logout_user, current_user, login_required
#from werkzeug.security import generate_password_hash, check_password_hash

from interncsfsu.users.models import User, Student, Company
from interncsfsu.users.forms import StudentLoginForm, CompanyLoginForm, CompanyApplication

mod = Blueprint('views', __name__, url_prefix='')

@mod.route('/')
def index():
    return render_template('index.html')

@mod.route('/company/login/', methods=['GET', 'POST'])
def company_login():
    if not current_user.is_anonymous:
        return redirect(url_for('.index'))
    next = ''
    if request.method == 'GET':
        if 'next' in request.args:
             next = request.args['next']
    form = CompanyLoginForm(request.form)
    if form.validate_on_submit():
        company = User.query.filter_by(email=form.email.data, password=form.password.data).first()
        if company is not None:
            if not company.is_authenticated:
                flash('Not authenticated')
                return redirect(url_for('.company_login'))
            if login_user(company):
                print('Logged in')
                return redirect(url_for('.index'))
            else:
                flash("Incorrect Username or Password")
                return render_template('login.html')

    if 'next' in request.form and request.form and request.form['next']:
        return redirect(request.form['next'])

    return render_template('login.html', form=form, next=next)

@mod.route('/student/login/', methods=['GET', 'POST'])
def student_login():
    if not current_user.is_anonymous:
        return redirect(url_for('.index'))
    #Obtain redirect
    next = ''
    if request.method == 'GET':
        if 'next' in request.args:
             next = request.args['next']

    #Get information from form and attempt to login
    form = StudentLoginForm(request.form)
    if form.validate_on_submit():
        #Passwords are not validated the normal way
        student = User.query.filter_by(email=form.email.data, password=form.password.data).first()
        if student is None:
            flash('Incorrect Email/Password')
        elif login_user(student):
                return redirect(url_for('.index'))
        else:
            flash('Error Logging in')

    if 'next' in request.form and request.form and request.form['next']:
        return redirect(request.form['next'])

    return render_template('login.html', form=form,next=next)


@mod.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))


@mod.route('/company/apply', methods=['GET', 'POST'])
def company_apply():
    if not current_user.is_anonymous:
        return redirect(url_for('.index'))

    form = CompanyApplication(request.form)
    company = Company(form.company_name.data, form.contact.data, form.company_website.data, form.com)




