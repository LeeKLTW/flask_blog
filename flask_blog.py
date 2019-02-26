# encoding: utf-8
from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User,Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '33f0baa056c172061e5b2394b9cb9915'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


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
        flash(f'Account {form.username.data} registered successfully.', category='success')
        return redirect(url_for('home'))
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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
