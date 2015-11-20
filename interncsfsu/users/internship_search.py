from flask import (Blueprint, flash, render_template, redirect, url_for, request, abort)
from interncsfsu.database import db
from interncsfsu.objects.models import Resume, Internship
from flask_login import login_user, logout_user, current_user, login_required
from interncsfsu.users.decorators import requires_roles

mod = Blueprint('views', __name__, url_prefix='')

@mod.route('/student/search/', methods=['GET','POST'])
@login_required
@requires_roles('Company')
def searchkeyword(keyword):
    internships = Internship.query.all()
    for i in internships:
        print(i)
    return render_template('internship_search.html')

