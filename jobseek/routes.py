from flask import render_template, url_for, redirect, flash
from jobseek import app, db
from jobseek.forms import registerForm, loginForm, jobForm
from jobseek.models import employer, job_post
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    job_posts = job_post.query.all()
    return render_template('home.html', job_posts=job_posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('home')
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = loginForm()
    if form.validate_on_submit():
        emp = employer.query.filter_by(email=form.companyEmail.data).first()
        if emp:
            login_user(emp)
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check company name and email', 'danger')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/create_job", methods=['GET', 'POST'])
@login_required
def create_job():
    form = jobForm()
    if form.validate_on_submit():
        new_job = job_post(title=form.title.data, sector=form.sector.data, jobType=form.jobType.data, location=form.location.data,
                            salary=form.salary.data, role_sum=form.summary.data, resp=form.responsibilities.data, requirements=form.requirements.data,
                            how_to_apply=form.how_to_apply.data, author=current_user)
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template(('create_job.html'), form=form)