from flask import render_template, url_for, redirect, flash, request
from jobseek import app, db
from jobseek.forms import registerForm, loginForm, jobForm, refineForm
from jobseek.models import employer, job_post, location, sector
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import or_, and_

# choices for refineForm select fields
# stopping duplicate values in select
def choices():
    salary_choices = [('salary', 'Salary')]
    sector_choices = [(0, 'Sector')]
    jobType_choices = [('jobType', 'Job Type')]
    location_choices = [(0, 'Location')]
    job_posts = job_post.query.all()
    for g in job_posts:
        if (g.salary, g.salary) not in salary_choices:
            salary_choices.append((g.salary, g.salary))
        if (g.sector_ref.id, g.sector_ref.sector ) not in sector_choices:
            sector_choices.append((g.sector_ref.id, g.sector_ref.sector))
        if (g.jobType, g.jobType ) not in jobType_choices:
            jobType_choices.append((g.jobType, g.jobType))
        if (g.location_ref.id, g.location_ref.city ) not in location_choices:
            location_choices.append((g.location_ref.id, g.location_ref.city))
    return salary_choices, sector_choices, jobType_choices, location_choices

# index route for home page
@app.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int) # find page for pagination 
    job_posts = job_post.query.order_by(job_post.date_posted.desc()).paginate(page=page, per_page=2)
    job_posts_total = job_posts.total # total posts for refine results 
    form = refineForm()
    # refine form select choices from choices helper function
    form.salary.choices = choices()[0]
    form.sector.choices = choices()[1]
    form.jobType.choices = choices()[2]
    form.location.choices = choices()[3]

    # current filters placeholders
    jobTypeField = form.jobType.data
    salaryField = form.salary.data
    sectorField = form.sector.data
    locationField = form.location.data

    # refine results form handler
    # checking if field selected. If not return all posts
    if form.validate_on_submit():
        if form.jobType.data == 'jobType':
            jobType = job_post.jobType
        else:
            jobType = form.jobType.data
            
        if form.sector.data == 0:
            sector_id = job_post.sector_id
        else:
            sector_id = form.sector.data

        if form.salary.data == 'salary':
            salary = job_post.salary
        else:
            salary = form.salary.data
            
        if form.location.data == 0:
            location_id = job_post.location_id
        else:
            location_id = form.location.data

        # new job_posts with filters
        job_posts = job_post.query.filter(and_(job_post.jobType == jobType,
                                                job_post.sector_id == sector_id,
                                                job_post.salary == salary,
                                                job_post.location_id == location_id
                                                )).order_by(job_post.date_posted.desc()).paginate(page=page, per_page=2)
        
        # current sector and location filters placeholders
        sectorField = sector.query.get(form.sector.data)
        locationField = location.query.get(form.location.data)
    
    return render_template('home.html', job_posts=job_posts,  job_posts_total= job_posts_total, form=form, jobTypeField=jobTypeField, 
                            salaryField=salaryField, sectorField=sectorField, locationField=locationField)

# register page 
@app.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)
    
# login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    ''' If current logged in user tries to access login page via URL then redirect to home page.
        If user is unregistered then send to register page and flash message.
        If user is registered then login user and redirect to home page
    '''
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = loginForm()
    if form.validate_on_submit():
        emp = employer.query.filter_by(email=form.companyEmail.data).first()
        if emp:
            login_user(emp, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash(f'Login unsuccessful. Please check company name and email', 'danger')
    return render_template('login.html', form=form)

# logout user
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

# create job page
@app.route("/create_job/new", methods=['GET', 'POST'])
@login_required
def create_job():
    ''' If all form fields are filled in and validates then create and commit a new job post to db.
        Redirecet to home page with flash message success
    '''
    form = jobForm()
    if form.validate_on_submit():
        new_job = job_post(title=form.title.data, sector_id=form.sector.data.id, jobType=form.jobType.data, location_id=form.location.data.id ,
                            salary=form.salary.data, role_sum=form.summary.data, resp=form.responsibilities.data, requirements=form.requirements.data,
                            how_to_apply=form.how_to_apply.data, author=current_user)
        db.session.add(new_job)
        db.session.commit()
        flash(f'Job post created by { new_job.author.companyName }!', 'success')
        return redirect(url_for('index'))
    return render_template(('create_job.html'), form=form, title='Create Job Post')

# view a full job post
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
        form.sector.data = job.sector_ref.sector
        form.jobType.data = job.jobType
        form.location.data = job.location_ref.city
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
    flash(f'Job post "{ job.title }" at "{job.author.companyName }" deleted."', 'success')
    return redirect(url_for('index'))