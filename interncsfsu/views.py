from flask import (Blueprint, flash, render_template, redirect, url_for, request, abort, session)
from flask_login import login_user, logout_user, current_user, login_required
#from werkzeug.security import generate_password_hash, check_password_hash

from interncsfsu.database import db
from interncsfsu.users.models import User, Student, Company
from interncsfsu.users.forms import (StudentLoginForm, CompanyLoginForm, CompanyApplication,
                                     StudentSettingsForm, CompanySettingsForm, InternshipForm, ContactForm,
                                     InternshipEditForm)
from interncsfsu.users.decorators import requires_roles
from interncsfsu.util.security import send_email, ts, admins
from config import SECRET_KEY


from interncsfsu.objects.models import Resume, Internship
from werkzeug.utils import secure_filename
from config import UPLOAD_PATH
import os

mod = Blueprint('views', __name__, url_prefix='')

@mod.route('/student/home/')
@login_required
@requires_roles('Student')
def home():
    user = User.query.filter_by(id=current_user.get_id()).first_or_404()
    return render_template('student_homepage.html', student=user.student)

@mod.route('/company/home/')
@login_required
@requires_roles('Company')
def emp_home():
    internships = current_user.company.internships
    return render_template('employer_homepage.html', company=current_user.company, internships=internships)

@mod.route('/')
def index():
    if not current_user.is_anonymous:
        if current_user.role == 'Student':
            return redirect(url_for('.home'))
        elif current_user.role == 'Company':
            return redirect((url_for('.emp_home')))
    return render_template('index.html')

@mod.route('/company/login/', methods=['GET', 'POST'])
def company_login():
    if not current_user.is_anonymous:
        if current_user.role == 'Student':
            return redirect(url_for('.home'))
        elif current_user.role == 'Company':
            return redirect((url_for('.emp_home')))

    next = ''
    if request.method == 'GET':
        if 'next' in request.args:
             next = request.args['next']
    form = CompanyLoginForm(request.form)
    if form.validate_on_submit():
        company = User.query.filter_by(email=form.email.data, password=form.password.data).first()
        if company is not None:
            if not company.authenticated:
                flash('Not authenticated')
                return redirect(url_for('.index'))
            if login_user(company):
                return redirect(url_for('.emp_home'))
            else:
                flash("Incorrect Username or Password")
                return render_template('login.html')

    if 'next' in request.form and request.form and request.form['next']:
        return redirect(request.form['next'])

    return render_template('employer_reg.html', form=form, next=next)

@mod.route('/student/login/', methods=['GET', 'POST'])
def student_login():
    if not current_user.is_anonymous:
        if current_user.role == 'Student':
            return redirect(url_for('.home'))
        elif current_user.role == 'Company':
            return redirect((url_for('.emp_home')))

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
                session['applied_to'] = []
                return redirect(url_for('.home'))
        else:
            flash('Error Logging in')

    if 'next' in request.form and request.form and request.form['next']:
        return redirect(request.form['next'])

    return render_template('student_reg.html',form=form)


@mod.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))

'''
Application form for companies.
Applications are sent to the administrator
for confirmation via email.
'''
@mod.route('/company/apply/', methods=['GET', 'POST'])
def company_apply():
    if not current_user.is_anonymous:
        if current_user.role == 'Student':
            return redirect(url_for('.home'))
        elif current_user.role == 'Company':
            return redirect((url_for('.emp_home')))

    form = CompanyApplication(request.form)
    if form.validate_on_submit():
        company = User(email=form.contact.data, password=form.password.data, role='Company', authenticated=False)
        company.company = Company(company.id, form.company_name.data, form.company_website.data)
        db.session.add(company)
        db.session.commit()
        #send confirmation email to the administrator
        subject = '[CSFSUINTERN] A New Company Has Registered'
        token = ts.dumps(company.email)
        confirm_url = url_for('.confirm_user', token=token, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        send_email(subject, html)
        return redirect(url_for('.index'))


    return render_template('register.html', form=form)

'''
Used by the administrator to confirm Company registrations
and authenticate them to use the website.
The link to this view will have been emailed to the administrator.
'''
@mod.route('/company/confirm/<token>/')
def confirm_user(token):
    if not current_user.is_anonymous:
        abort(404)
    try:
        email = ts.loads(token)
    except:
        abort(404)

    # Query the database for the User and Update authentication
    user = User.query.filter_by(email=email).first_or_404()
    user.authenticated = True
    user.is_authenticated = True
    db.session.add(user)
    db.session.commit()

    #Add a "Thanks for confirming" page
    return redirect(url_for('.company_login'))


@mod.route('/student/settings/', methods=['GET','POST'])
@login_required
@requires_roles('Student')
def student_settings():
    user = User.query.filter_by(id=current_user.get_id()).first_or_404()
    form = StudentSettingsForm(request.form)
    if user.student.About:
        form.about.data = user.student.About
    if form.validate_on_submit():
        if form.about.data:
            user.student.About = form.about.data

        if form.resume.name in request.files:
            file = request.files[form.resume.name]
            try:
                extension = file.filename.split('.')[1]
            except:
                extension = 'pdf'
            filename = '%d.%s' % (user.id, extension)
            full_path = os.path.join(UPLOAD_PATH, filename)
            if user.student.resume:
                db.session.delete(user.student.resume)
            rel_path = '/static/uploads/%d.%s' % (user.id, extension)
            user.student.resume = Resume(rel_path)
            file.save(full_path)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.home'))
    return render_template('student_settings.html', form=form, student=user.student)

@mod.route('/company/settings/', methods=['GET','POST'])
@login_required
@requires_roles('Company')
def company_settings():
    user = User.query.filter_by(id=current_user.get_id()).first_or_404()
    form = CompanySettingsForm(request.form)
    form.name.data = user.company.name
    form.website.data = user.company.website
    form.contact.data = user.email
    if form.validate_on_submit():
        if form.name.data:
            user.company.name = form.name.data
        if form.website.data:
            user.company.website = form.website.data
        if form.contact.data:
            user.email = form.contact.data
        if form.new_password.data:
            user.password = form.new_password.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.emp_home'))
    return render_template('company_settings.html', form=form)

@mod.route('/company/internship/', methods=['GET','POST'])
@login_required
@requires_roles('Company')
def company_internship():
    internships = Internship.query.filter_by(companyid=current_user.get_id()).all()
    remove= "0"
    remove= request.args.get('remove')
    print('remove')
    print(remove)
    int_id = request.args.get('int_id')
    print(int_id)
    if remove == "1":
        int_id = request.args.get('int_id')
        print(int_id)
        internship = Internship.query.filter_by(id=int_id).first_or_404()
        db.session.delete(internship)
        db.session.commit()
        return redirect('/company/internship/')
    return render_template('company_internships.html', internships=internships)

@mod.route('/company/internship/delete/<id>', methods=['GET', 'POST'])
@login_required
@requires_roles('Company')
def delete_internship(id):
    internship = Internship.query.get(id)
    db.session.delete(internship)
    db.session.commit()
    return redirect(url_for('.emp_home'))


@mod.route('/company/internship/add/', methods=['GET','POST'])
@login_required
@requires_roles('Company')
def company_add_internship():
    form = InternshipForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.get_id()).first_or_404()
        internship = Internship(user.id, form.position.data, form.startdate.data, form.location.data, form.applicationlink.data,form.description.data)
        user.company.internships.append(internship)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.emp_home'))
    return render_template('company_internships_add.html', form=form)

@mod.route('/company/internship/edit/<id>', methods=['GET', 'POST'])
@login_required
@requires_roles('Company')
def edit_internship(id):
    internship = Internship.query.get(id)
    form = InternshipEditForm(request.form, obj=internship)
    if form.validate_on_submit():
        form.id.data = internship.id
        form.populate_obj(internship)
        db.session.add(internship)
        db.session.commit()
        return redirect(url_for('.emp_home'))
    return render_template('edit_internship.html', form=form)

@mod.route('/student/search/', methods=['GET','POST'])
@login_required
@requires_roles('Student')
def searchkeyword():
    internships = Internship.query.join(Company).all()
    return render_template('internship_search.html', internships=internships)

@mod.route('/student/search/listing/<id>', methods=['GET','POST'])
@login_required
@requires_roles('Student')
def showinternship(id):
    internship = Internship.query.get(id)
    user = User.query.filter_by(id=internship.companyid).first_or_404()
    return render_template('internship_listing.html',internship=internship, user=user)

@mod.route('/company/search/', methods=['GET', 'POST'])
@login_required
@requires_roles('Company')
def company_search():
    students = Student.query.join(User).all()
    return render_template('student_search.html', students=students)

@mod.route('/company/search/student/<id>')
@login_required
@requires_roles('Company')
def showstudent(id):
    user = User.query.filter_by(id=id).first()
    return render_template('student_listing.html', student=user.student)

@mod.route('/company/send/<id>', methods=['GET', 'POST'])
@login_required
@requires_roles('Company')
def send_to_student(id):
    company = Company.query.get(current_user.get_id())
    user = User.query.filter_by(id=id).first_or_404()
    subject = '[INTERNCSFSU] A Company Has Expressed Interest'
    html = render_template('company_interest.html', company=company)
    send_email(subject=subject, html_body=html, recipients=[user.email])
    return redirect(url_for('.company_search'))

from flask_mail import Message
from interncsfsu import app, mail
from config import ADMINS as admins

@mod.route('/student/send/<id>', methods=['GET', 'POST'])
@login_required
@requires_roles('Student')
def send_to_company(id):
    student = Student.query.get(current_user.get_id())
    user = User.query.filter_by(id=id).first_or_404()
    subject = '[INTERNCSFSU] A Student Has Expressed Interest'
    html = render_template('student_interest.html', student=student)
    msg = Message(subject, sender=admins[0], recipients=[user.email])
    msg.html = html
    if student.resume:
        #system dependent path
        path = 'C:\\Users\\Christian\\Desktop\\interncsfsu\\interncsfsu\\static\\uploads\\%i.pdf' % (student.ID)
        with app.open_resource(path) as fp:
            msg.attach("resume.pdf", "application/pdf", fp.read())

    mail.send(msg)
    return redirect(url_for('.searchkeyword'))

@mod.route('/company/message/', methods=['GET', 'POST'])
@login_required
@requires_roles('Company')
def message_all():
    form = ContactForm(request.form)
    recipients = []
    if form.validate_on_submit():
        if '0' in form.students.data:
            recipients += Student.query.filter_by(Year="Freshman").all()
        if '1' in form.students.data:
            recipients += Student.query.filter_by(Year="Sophomore").all()
        if '2' in form.students.data:
            recipients += Student.query.filter_by(Year="Junior").all()
        if '3' in form.students.data:
            recipients += Student.query.filter_by(Year="Senior").all()

        subject = '[CSFSUINTERN] %s' % (form.subject.data)
        body = form.body.data
        recipients = [student.user.email for student in recipients]
        send_email(subject=subject, html_body=body, recipients=recipients)
        return redirect(url_for('.message_all'))

    return render_template('message_all.html', form=form)

@mod.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = CompanyLoginForm(request.form)
    if form.validate_on_submit():
        admin = User.query.filter_by(email=form.email.data, password=form.password.data,role='Admin').first_or_404()
        if (login_user(admin)):
            return redirect(url_for('.admin_home'))
        else:
            abort(404)
    return render_template('admin_login.html', form=form)


@mod.route('/admin/', methods=['GET', 'POST'])
@login_required
@requires_roles('Admin')
def admin_home():
    companies = Company.query.all()
    return render_template('admin_home.html', companies=companies)

@mod.route('/admin/delete/company/<id>', methods=['GET', 'POST'])
@login_required
@requires_roles('Admin')
def admin_remove(id):
    company = Company.query.get(id)
    company.is_authenticated = False
    company.user.authenticated = False
    db.session.add(company)
    db.session.commit()
    return redirect(url_for('.admin_home'))