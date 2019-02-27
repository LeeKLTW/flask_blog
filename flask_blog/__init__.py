# encoding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '33f0baa056c172061e5b2394b9cb9915'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app=app)
bcrypt = Bcrypt(app=app)
login_manager = LoginManager(app=app)

from flask_blog import routes
