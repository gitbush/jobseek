from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from jobseek.models import employer, job_post

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

# wtforms create a job class
class jobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    sector = StringField('Sector', validators=[DataRequired()])
    jobType = SelectField('Type', choices=[('Select', 'Select'), ('Full-time','Full-time' ), ('Part-time', 'Part-time'), ('Contract', 'Contract')], default=1)
    location = StringField('Location eg London, UK', validators=[DataRequired()])
    salary = SelectField('Salary', validators=[DataRequired], choices=[('Salary', 'Salary'), ('30000+','30000+' ), ('40000+', '40000+'), ('50000+', '50000+')], default=1)
    summary = TextAreaField('Role Summary', validators=[DataRequired()])
    responsibilities = TextAreaField('Skills/Responsibilities', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    how_to_apply = TextAreaField('How to Apply', validators=[DataRequired()])
    submit = SubmitField('Create Job!')

def choice():
    return job_post.query

class refineForm(FlaskForm):
    jobType = SelectField('Type', choices=[('Type', 'Type'), ('Full-time','Full-time' ), ('Part-time', 'Part-time'), ('Contract', 'Contract')], default=1)
    sector = QuerySelectField(label='Job Type', blank_text='Sector', allow_blank=True, query_factory=choice, get_label=lambda a: a.sector)
    salary = SelectField('Salary', choices=[('Salary', 'Salary'), ('<=39000','30000+' ), ('<=49000', '40000+'), ('<=59000', '50000+')], default=1)
    location = QuerySelectField(label='Job Type', blank_text='Location', allow_blank=True, query_factory=choice, get_label=lambda a: a.location)
    submit = SubmitField('Refine')