from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, InputForm, ProveanForm, GnomadForm, ClinvarForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = InputForm()
    return render_template('home.html', title = 'Input', form= form)

@app.route("/clinvar", methods=['GET', 'POST'])
def clinvar():
    form = ClinvarForm()
    return render_template('clinvar.html', title = 'Input', form= form)

@app.route("/provean", methods=['GET', 'POST'])
def provean():
    form = ProveanForm()
    return render_template('provean.html', title = 'Input', form= form)

@app.route("/gnomad", methods=['GET', 'POST'])
def gnomad():
    form = GnomadForm()
    return render_template('gnomad.html', title = 'Input', form= form)

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
