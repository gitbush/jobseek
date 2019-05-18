from flask import render_template, url_for, redirect, flash, request, Blueprint
from jobseek.models import employer, job_post, location, sector
from jobseek.job_posts.forms import jobForm
from flask_login import login_user, current_user, logout_user, login_required


posts = Blueprint('posts', __name__)


# create job page
@posts.route("/create_job/new", methods=['GET', 'POST'])
@login_required
def create_job():
    ''' If all form fields are filled in and validates then create and commit a new job post to db.
        Redirecet to home page with flash message success
    '''
    form = jobForm()
    if form.validate_on_submit():
        new_job = job_post(title=form.title.data, sector_id=form.sector.data.id, jobType=form.jobType.data, location_id=form.location.data.id ,
                            salary=form.salary.data, role_sum=form.summary.data, resp=form.responsibilities.data, requirements=form.requirements.data,
                            how_to_postsly=form.how_to_postsly.data, author=current_user)
        db.session.add(new_job)
        db.session.commit()
        flash(f'Job post created by { new_job.author.companyName }!', 'success')
        return redirect(url_for('main.index'))
    return render_template(('create_job.html'), form=form, title='Create Job Post')

# view a full job post
@posts.route("/job/<int:id>")
def job(id):
    job = job_post.query.get(id)
    return render_template('job_post.html', job=job)

# edit a job post
@posts.route("/job/<int:id>/edit", methods=['GET', 'POST'])
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
        job.how_to_postsly = form.how_to_postsly.data 
        db.session.commit()
        return redirect(url_for('posts.job', id=job.id))

    elif request.method == 'GET':
        form.title.data = job.title
        form.sector.data = job.sector_ref.sector
        form.jobType.data = job.jobType
        form.location.data = job.location_ref.city
        form.salary.data = job.salary
        form.summary.data = job.role_sum
        form.responsibilities.data = job.resp
        form.requirements.data = job.requirements
        form.how_to_postsly.data = job.how_to_postsly        

    return render_template('create_job.html', form=form, title='Edit Job Post')

# delete a job post
@posts.route("/job/<int:id>/delete", methods=['POST'])
@login_required
def delete_post(id):
    job = job_post.query.get(id)
    db.session.delete(job)
    db.session.commit()
    flash(f'Job post "{ job.title }" at "{job.author.companyName }" deleted."', 'success')
    return redirect(url_for('main.index'))