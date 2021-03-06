from app import app
from flask import Flask
from flask import render_template, flash, redirect
from flask_login import login_user, logout_user, current_user, login_required, UserMixin, LoginManager
from forms import LoginForm
from models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Miguel' }
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]    
    return render_template('index.html', title='home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        flash('Login requested for OpenID=%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))  
        return redirect('/index')
#    return render_template('login.html', title='Sign In', form=form)
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query().get(int(id))