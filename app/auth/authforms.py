from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email =  StringField('Email', validators=[DataRequired()])
    first_name =  StringField('First Name')
    last_name =  StringField('Last Name')
    password =  StringField('Password', validators=[DataRequired()])
    confirm_password =  StringField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField()