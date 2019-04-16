from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class registerForm(FlaskForm):
    companyName = StringField('Company Name', validators=[DataRequired(), Length(min=3, max=20)])
    companyEmail = StringField('Company Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')