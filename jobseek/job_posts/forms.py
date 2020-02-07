from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired 
from jobseek.models import job_post, location, sector


# querySelectField query factories
def location_choice():
    return location.query

def sector_choice():
    return sector.query

def choice():
    return job_post.query

class JobForm(FlaskForm):
    """
    Job post form
    """
    title = StringField('Job Title', validators=[DataRequired()])
    sector = QuerySelectField('Sector', query_factory=sector_choice, get_label=lambda a: a.sector)
    jobType = SelectField('Job Type', choices=[('(Please select)', '(Please select)'), ('Full-time','Full-time' ), ('Part-time', 'Part-time'), ('Contract', 'Contract')], default=1)
    location = QuerySelectField('Location', query_factory=location_choice)
    salary = SelectField('Salary', choices=[('(Please select)', '(Please select)'), ('10000+','10000+' ), ('20000+','20000+' ), ('30000+','30000+' ),
                                             ('40000+', '40000+'), ('50000+', '50000+')], default=1)
    summary = TextAreaField('Role Summary', validators=[DataRequired()])
    responsibilities = TextAreaField('Skills/Responsibilities', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    how_to_apply = TextAreaField('How to Apply', validators=[DataRequired()])
    submit = SubmitField('Create Job!')
