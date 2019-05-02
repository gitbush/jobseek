from flask import render_template, url_for, redirect, flash, request
from jobseek import app, db
from jobseek.forms import registerForm, loginForm, jobForm, refineForm
from jobseek.models import employer, job_post
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import or_, and_


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    job_posts = job_post.query.all()
    form = refineForm()
    # return tuples with key, value pairs for choices
    form.sector.choices = [(item.id, item.sector) for item in job_post.query.all()]
    form.salary.choices = [(item.id, item.salary) for item in job_post.query.all()]
    form.location.choices = [(item.id, item.location) for item in job_post.query.all()]
    if form.validate_on_submit():
        # form handling of none selected 
        if form.jobType.data == None:
            jobType = job_post.jobType
        else:
            jobType = form.jobType.data.jobType

        if form.sector.data == None:
            sector = job_post.sector
        else:
            sector = form.sector.data.sector

        if form.salary.data == None:
            salary = job_post.salary
        else:
            salary = form.salary.data.salary
            
        if form.location.data == None:
            location = job_post.location
        else:
            location = form.location.data.location
        
        job_posts = job_post.query.filter(and_(job_post.jobType == jobType,
                                                job_post.sector == sector,
                                                job_post.salary == salary,
                                                job_post.location == location)).all()


    return render_template('home.html', job_posts=job_posts, form=form)

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


@app.route("/create_job/new", methods=['GET', 'POST'])
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
    return render_template(('create_job.html'), form=form, title='Create Job Post')

# # view a full job post
@app.route("/job/<int:id>")
def job(id):
    job = job_post.query.get(id)
    return render_template('job_post.html', job=job)

# edit a job post
@app.route("/job/<int:id>/edit", methods=['GET', 'POST'])
@login_required
def edit_post(id):
    ''' Populate form with corresponding job data if request method is GET
        If POST commmit changes to db and redirect to updated job post
    '''
    job = job_post.query.get(id)
    form = jobForm()

    if form.validate_on_submit():
        job.title = form.title.data
        job.sector = form.sector.data 
        job.jobType = form.jobType.data  
        job.location = form.location.data 
        job.salary = form.salary.data 
        job.role_sum = form.summary.data 
        job.resp = form.responsibilities.data 
        job.requirements = form.requirements.data 
        job.how_to_apply = form.how_to_apply.data 
        db.session.commit()
        return redirect(url_for('job', id=job.id))

    elif request.method == 'GET':
        form.title.data = job.title
        form.sector.data = job.sector
        form.jobType.data = job.jobType
        form.location.data = job.location
        form.salary.data = job.salary
        form.summary.data = job.role_sum
        form.responsibilities.data = job.resp
        form.requirements.data = job.requirements
        form.how_to_apply.data = job.how_to_apply        

    return render_template('create_job.html', form=form, title='Edit Job Post')

# delete a job post
@app.route("/job/<int:id>/delete", methods=['POST'])
@login_required
def delete_post(id):
    job = job_post.query.get(id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('home'))