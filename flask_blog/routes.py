# encoding: utf-8
from flask import render_template, redirect, url_for, flash
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import Post, User
from flask_blog import app, db, bcrypt


posts = [
    {
        'author': 'Kevin Lee',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Kevin Lee',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account {form.username.data} registered successfully.', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.email.data == 'admin@blog.com' and form.password.data == '123':
        flash(f'Account {form.email.data} Logged in.', 'success')
        return redirect(url_for('home'))
    else:
        flash(f'not correct', 'danger')
    return render_template('login.html', title='Login', form=form)


