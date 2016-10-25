from app import app
from flask import Flask
from flask import render_template

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