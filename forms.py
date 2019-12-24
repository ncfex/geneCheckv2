from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from DataOps import clinvar, gnomad, provean

#from responses import  html, res_poly, res_mut, unparsed_poly, unparsed_muta, output_file, web_result_page_html

class InputForm(FlaskForm):
    clinvar_id = StringField('clinvar_data', validators=[DataRequired(), Length(min=2, max=20)])
    provean_id = StringField('provean_data', validators=[DataRequired(), Length(min=2, max=20)])
    gnomad_id = StringField('gnomad_data', validators=[DataRequired(), Length(min=2, max=20)])

class ResultForm(FlaskForm):
    a= 1

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
