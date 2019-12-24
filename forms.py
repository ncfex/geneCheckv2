from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from DataOps import clinvar, provean
import time

#from responses import  html, res_poly, res_mut, unparsed_poly, unparsed_muta, output_file, web_result_page_html

class InputForm(FlaskForm):
    clinvar_id = StringField('clinvar_data', validators=[DataRequired(), Length(min=2, max=20)])

class ResultForm(FlaskForm):
    c1 = clinvar.Clinvar()
    p1 = provean.Provean()
    clinvar_prediction = c1.parse_clinvar()
    provean_sco = p1.parse_PROV_Score()
    provean_pre = p1.parse_PROV_Predic()
    sift_sco = p1.parse_SIFT_Score()
    sift_pre = p1.parse_SIFT_Predic()

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
