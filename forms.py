from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from DataOps import varsome
import time

#from responses import  html, res_poly, res_mut, unparsed_poly, unparsed_muta, output_file, web_result_page_html

class InputForm(FlaskForm):
    rs_no = "1"

class ResultForm(FlaskForm):

    '''
    c1 = clinvar.Clinvar()
    p1 = provean.Provean()
    '''


    '''
    clinvar_prediction = c1.parse_clinvar()

    provean_sco = p1.parse_PROV_Score()
    provean_pre = p1.parse_PROV_Predic()
    sift_sco = p1.parse_SIFT_Score()
    sift_pre = p1.parse_SIFT_Predic()

class ClinvarForm(FlaskForm):
    rs_no = StringField('RS NO: ',
                           validators=[Length(min=2, max=20)], render_kw={"placeholder": "rs1800215"})
    submit = SubmitField('Search')
    clinvar = ResultForm.clinvar_prediction

class ProveanForm(FlaskForm):
    rs_no = StringField('RS NO: ',
                           validators=[Length(min=2, max=20)], render_kw={"placeholder": "rs1800215"})
    submit = SubmitField('Search')
    provean_sco = ResultForm.provean_sco
    provean_pre = ResultForm.provean_pre
    sift_sco = ResultForm.sift_sco
    sift_pre = ResultForm.sift_pre
    '''
    '''
class VarsomeForm(FlaskForm):
    clinvar_verdict = ResultForm.clinvar_verdict
    DANN_score = ResultForm.DANN_score
    GERP_score = ResultForm.GERP_score
    gnomAD_freq = ResultForm.gnomAD_freq
    ACMG_verdict = ResultForm.ACMG_verdict
    '''

'''---------------------------------------------login register------------------------------------------'''

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
