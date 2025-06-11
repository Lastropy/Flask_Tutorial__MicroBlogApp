from flask import render_template,flash, redirect, url_for
from app import app
from app.forms.loginform import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form_obj = LoginForm()
    if login_form_obj.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            login_form_obj.username.data, login_form_obj.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=login_form_obj)