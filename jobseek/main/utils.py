from jobseek.models import job_post, location, sector
from operator import itemgetter


# choices for refineForm select fields
# stopping duplicate values in select
def choices():
    salary_choices = [('0', 'Salary')]
    sector_choices = [(0, 'Sector')]
    jobType_choices = [('0', 'Job Type')]
    location_choices = [(0, 'Location')]
    job_posts = job_post.query.all()

    # if user selection not 0 or field name add the available list
    for g in job_posts:
        if (g.salary, g.salary) not in salary_choices:
            salary_choices.append((g.salary, g.salary))
            salary_choices.sort(key = itemgetter(0))
        if (g.sector_ref.id, g.sector_ref.sector ) not in sector_choices:
            sector_choices.append((g.sector_ref.id, g.sector_ref.sector))
            sector_choices.sort(key = itemgetter(0))
        if (g.jobType, g.jobType ) not in jobType_choices:
            jobType_choices.append((g.jobType, g.jobType))
        if (g.location_ref.id, g.location_ref.city ) not in location_choices:
            location_choices.append((g.location_ref.id, g.location_ref.city))
            location_choices.sort(key = itemgetter(0))
    return salary_choices, sector_choices, jobType_choices, location_choices
