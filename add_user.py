# encoding: utf-8
from flask_blog import db
from flask_blog import User, Post

user_list = [{'username':'Kevin', 'email':'Kevin@gmail.com','password':'password'}]
u = User(**user_list[0])
db.session.add(u)
db.session.commit()

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# User.query.all()
# User.query.filter_by(username='Kevin').all()

