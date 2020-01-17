from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, InputForm, ResultForm
import requests
import threading
import DataOps.clinvar, DataOps.provean
from DataOps import varsome

from varsome_api.client import VarSomeAPIClient

VarSomeAPI = VarSomeAPIClient('ABgxPSr6UD*mseWP22!ZC?01Or#1O&&hYUrCorQf')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html', title='Search Databases for Genomes')

    rs_no = request.form.get('rs_no')

    from DataOps import varsome
    varsome = varsome.Varsome()

    if request.method == 'POST':
        varsome_variant = varsome.send_req(rs_no)
        r = rs_no
        ACMG_verdict = varsome.ACMG_verdict_f(varsome_variant)
        clinvar_verdict = varsome.clinvar_verdict_f(varsome_variant)
        DANN_score = varsome.DANN_score_f(varsome_variant)
        GERP_score = varsome.GERP_score_f(varsome_variant)
        gnomAD_freq = varsome.gnomAD_Freq_f(varsome_variant)
        mutationtaster_pred = varsome.mutationtaster_pred_f(varsome_variant)
        SIFT_pred = varsome.SIFT_pred_f(varsome_variant)
        SIFT_score = varsome.SIFT_score_f(varsome_variant)
        PROVEAN_pred = varsome.PROVEAN_pred_f(varsome_variant)
        PROVEAN_score = varsome.PROVEAN_score_f(varsome_variant)

        import time
        time.sleep(1.5)
        return render_template("result.html", ACMG_verdict=ACMG_verdict, clinvar_verdict=clinvar_verdict, DANN_score=DANN_score,
                               GERP_score=GERP_score, gnomAD_freq=gnomAD_freq, mutationtaster_pred=mutationtaster_pred, SIFT_pred=SIFT_pred,
                               SIFT_score=SIFT_score, PROVEAN_pred=PROVEAN_pred, PROVEAN_score=PROVEAN_score, r=r)

    return render_template('home.html', title = 'Search Databases for Genomes')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
