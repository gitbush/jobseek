from flask import render_template, url_for, redirect, flash, request, Blueprint
from jobseek.models import employer, job_post, location, sector
from sqlalchemy import or_, and_
from jobseek.main.utils import choices
from jobseek.main.forms import RefineForm


main = Blueprint('main', __name__)

# index route for home page
@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int) # find page for pagination 
    job_posts = job_post.query.order_by(job_post.date_posted.desc()).paginate(page=page, per_page=2)
    job_posts_total = job_posts.total # total posts for refine results 
    form = RefineForm()
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
        if form.jobType.data == '0':
            jobType = job_post.jobType
        else:
            jobType = form.jobType.data
            
        if form.sector.data == 0:
            sector_id = job_post.sector_id
        else:
            sector_id = form.sector.data

        if form.salary.data == '0':
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


