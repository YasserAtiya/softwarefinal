from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__,static_url_path='/static')
app.config.from_object('config')

db = SQLAlchemy(app)

from interncsfsu.views.views import mod as views_mod
app.register_blueprint(views_mod)

app.debug = True

if __name__ == '__main__':
    app.run()