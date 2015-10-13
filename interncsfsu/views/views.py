from flask import (Blueprint, render_template, g, session, redirect, url_for, request)
from werkzeug.security import generate_password_hash, check_password_hash

from interncsfsu import db
from interncsfsu.student.forms import StudentRegisterForm, StudentLoginForm
from interncsfsu.student.models import Student

mod = Blueprint('views', __name__, url_prefix='')

@mod.route('/')
def index():
    return render_template('index.html')

@mod.route('/register/', methods=['GET', 'POST'])
def register():
    next = ''
    if request.method == 'GET':
        if 'next' in request.args:
             next = request.args['next']

    form = StudentRegisterForm(request.form)
    if form.validate_on_submit():
        student = Student(sid=form.email.data, name=form.name.data, gpa=form.gpa.data, interest=form.interest.data,
                          password=generate_password_hash(form.password.data))
        db.session.add(student)
        try:
            db.session.commit()
        except:
            db.session.flush()
        finally:
            db.session.close()


        if 'next' in request.form and request.form and request.form['next']:
            return redirect(request.form['next'])
        return redirect(url_for('mod./'))

    return render_template("register.html", form=form, next=next)




