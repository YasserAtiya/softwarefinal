import re

from flask import Flask
from flask_login import LoginManager
from interncsfsu.database import db
from flask_mail import Mail


import interncsfsu.users.models as models

app = Flask(__name__,static_url_path='/static')
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/'
db.init_app(app)
mail = Mail(app)

from interncsfsu.views import mod as views_mod
app.register_blueprint(views_mod)

app.debug = True


@login_manager.user_loader
def load_user(id):
    return models.User.query.filter_by(id=id).first()


if __name__ == '__main__':
    app.run()