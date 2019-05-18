from flask import render_template, url_for, redirect, flash, request, Blueprint
from jobseek import db
from jobseek.users.forms import registerForm, loginForm
from jobseek.models import employer, job_post
from flask_login import login_user, current_user, logout_user, login_required

employers = Blueprint('employers', __name__)

# register page 
@employers.route('/register', methods=['GET', 'POST'])
def register():
    ''' If current logged in user tries to access register page via URL then redirect to home page.
        If unregistered and register form validates, create and commit new employer to db
    '''
    if current_user.is_authenticated:
        return redirect('home')
    form = registerForm()
    if form.validate_on_submit():
        if form.logo.data == '':
            emp = employer(companyName=form.companyName.data, email=form.companyEmail.data)
        else:
            emp = employer(companyName=form.companyName.data, email=form.companyEmail.data, logo_url=form.logo.data)
        print(form.logo.data)
        db.session.add(emp)
        db.session.commit()
        flash(f'Account created for { form.companyName.data }! You can now login.', 'success')
        return redirect(url_for('employers.login'))
    
    return render_template('register.html', form=form)
    
# login page
@employers.route("/login", methods=['GET', 'POST'])
def login():
    ''' If current logged in user tries to access login page via URL then redirect to home page.
        If user is unregistered then send to register page and flash message.
        If user is registered then login user and redirect to home page
    '''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = loginForm()
    if form.validate_on_submit():
        emp = employer.query.filter_by(email=form.companyEmail.data).first()
        if emp:
            login_user(emp, remember=form.remember.data)
            return redirect(url_for('main.index'))
        else:
            flash(f'Login unsuccessful. Please check company name and email', 'danger')
    return render_template('login.html', form=form)

# logout user
@employers.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))
