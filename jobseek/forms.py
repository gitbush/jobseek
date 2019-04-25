from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from jobseek.models import employer

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