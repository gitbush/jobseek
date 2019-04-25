from flask import render_template, url_for, redirect, flash
from jobseek import app, db
from jobseek.forms import registerForm, loginForm
from jobseek.models import employer, job_post
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        emp = employer(companyName=form.companyName.data, email=form.companyEmail.data)
        db.session.add(emp)
        db.session.commit()
        flash(f'Account created for { form.companyName.data }! You can now login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)
    

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        emp = employer.query.filter_by(email=form.companyEmail.data).first()
        if emp:
            login_user(emp)
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check company name and email', 'danger')
    return render_template('login.html', form=form)