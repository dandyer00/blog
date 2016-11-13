#from flask.ext.wtf import Form
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from werkzeug import formparser
from duplicity.tempdir import default

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    
    