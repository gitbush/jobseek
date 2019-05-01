from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField
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
    salary = IntegerField('Salary', validators=[DataRequired()])
    summary = TextAreaField('Role Summary', validators=[DataRequired()])
    responsibilities = TextAreaField('Skills/Responsibilities', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    how_to_apply = TextAreaField('How to Apply', validators=[DataRequired()])
    submit = SubmitField('Create Job!')

# wtforms refine results form 
class refineForm(FlaskForm):
    jobType = SelectField(label='Job Type', choices=[('Type', 'Type'), ('Part-time', 'Part-time'), ('Full-time', 'Full-time'), ('Contract', 'Contract')])
    sector = SelectField(label='Sector', choices=[('Sector', 'Sector')])
    salary = SelectField(label='Salary', choices=[('Salary', 'Salary')])
    location = SelectField(label='Location', choices=[('Location', 'Location')])
    submit = SubmitField('Update')