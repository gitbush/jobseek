from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class registerForm(FlaskForm):
    companyName = StringField('companyName', validators=[DataRequired(), Length(min=3, max=20)])
    companyEmail = StringField('companyEmail', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')