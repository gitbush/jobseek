from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

class RefineForm(FlaskForm):
    """
    Job post search form
    """
    jobType = SelectField('Job Type')
    sector = SelectField('Sector', coerce=int)
    salary = SelectField('Salary')   
    location = SelectField('Location', coerce=int)
    submit = SubmitField('Filter')
