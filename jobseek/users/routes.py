from flask import render_template, url_for, redirect, flash, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from jobseek import db
from jobseek.users.forms import RegisterForm, LoginForm
from jobseek.models import employer, job_post

employers = Blueprint('employers', __name__)

# register page 
@employers.route('/register', methods=['GET', 'POST'])
def register():
    ''' If current logged in user tries to access register page via URL then redirect to home page.
        If unregistered and register form validates, create and commit new employer to db
    '''
    if current_user.is_authenticated:
        return redirect('home')
    form = RegisterForm()
    if form.validate_on_submit():
        if form.logo.data == '':
            emp = employer(companyName=form.companyName.data, email=form.companyEmail.data, logo_url='https://i.ibb.co/F6jkzLK/default.jpg')
        else:
            emp = employer(companyName=form.companyName.data, email=form.companyEmail.data, logo_url=form.logo.data)
        db.session.add(emp)
        db.session.commit()

        # log new user in and send to home page
        login_user(emp)
        flash(f'Logged in as {form.companyName.data}', 'success')
        return redirect(url_for('main.index'))
    
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
    form = LoginForm()
    if form.validate_on_submit():
        emp = employer.query.filter_by(email=form.companyEmail.data).first()
        if emp:
            login_user(emp, remember=form.remember.data)
            flash(f'Logged in as {form.companyName.data}', 'success')
            return redirect(url_for('main.index'))
        else:
            flash(f'Login unsuccessful. Please check company name and email', 'danger')
    return render_template('login.html', form=form)

# logout user
@employers.route("/logout")
def logout():
    logout_user()
    flash(f'You are now logged out', 'success')
    return redirect(url_for('main.index'))
