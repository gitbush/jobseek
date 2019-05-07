from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from jobseek.models import employer, job_post, location, sector

# wtforms registration class
class registerForm(FlaskForm):
    companyName = StringField('Company Name', validators=[DataRequired(), Length(min=3, max=20)])
    companyEmail = StringField('Company Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

    # custom validation checking if a user has already signed up with company name and email
    def validate_companyName(self, companyName):
        emp = employer.query.filter_by(companyName=companyName.data).first()
        if emp:
            raise ValidationError('Company already exists on Jobseek. Please login')

    def validate_Email(self, email):
        emp = employer.query.filter_by(email=companyEmail.data).first()
        if emp:
            raise ValidationError('Email already exists on Jobseek. Please use an alternate email')

# wtforms login class
class loginForm(FlaskForm):
    companyName = StringField('Company Name', validators=[DataRequired(), Length(min=3, max=20)])
    companyEmail = StringField('Company Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Login')


def location_choice():
    return location.query

def sector_choice():
    return sector.query

def choice():
    return job_post.query

# wtforms create a job class
class jobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    sector = QuerySelectField('Sector', blank_text='(Please select)', allow_blank=True, query_factory=sector_choice, get_label=lambda a: a.sector)
    jobType = SelectField('Job Type', choices=[('(Please select)', '(Please select)'), ('Full-time','Full-time' ), ('Part-time', 'Part-time'), ('Contract', 'Contract')], default=1)
    location = QuerySelectField('Location', blank_text='(Please select)', allow_blank=True, query_factory=location_choice)
    salary = SelectField('Salary', choices=[('(Please select)', '(Please select)'), ('30000+','30000+' ), ('40000+', '40000+'), ('50000+', '50000+')], default=1)
    summary = TextAreaField('Role Summary', validators=[DataRequired()])
    responsibilities = TextAreaField('Skills/Responsibilities', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    how_to_apply = TextAreaField('How to Apply', validators=[DataRequired()])
    submit = SubmitField('Create Job!')

class refineForm(FlaskForm):
    jobType = SelectField('Job Type')
    sector = SelectField('Job Type')
    salary = SelectField('Salary')   
    location = SelectField('Job Type')
    submit = SubmitField('Refine')



