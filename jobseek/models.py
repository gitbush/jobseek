from jobseek import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# using flask login manager to find user in db
@login_manager.user_loader
def user_loader(user_id):
    return employer.query.get(user_id)

class employer(db.Model, UserMixin):
    """
    Employer user db model 
    """
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    logo_url = db.Column(db.String(150), nullable=False, default='http://job.pharmaglobiz.com/images/default-logo.png')
    job_posts = db.relationship('job_post', backref='author', lazy=True)
    # string to return in shell when employer model called
    def __repr__(self):
        return f"User: {self.companyName}"

class job_post(db.Model):
    """
    Job_post db model
    """
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(60), nullable=False)
    jobType = db.Column(db.String(40), nullable=False)
    salary = db.Column(db.String(15), nullable=False)
    role_sum = db.Column(db.Text, nullable=False)
    resp = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    how_to_apply = db.Column(db.Text, nullable=False)
    emp_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False )
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False )
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False )
    # string to return in shell when job_post model called
    def __repr__(self):
        return f"Job Post: {self.date_posted}, {self.title}"

class sector(db.Model):
    """
    Sector db model to store sectors choice
    """
    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String(60), nullable=False)
    sector_backref = db.relationship('job_post', backref='sector_ref', lazy=True)
    def __repr__(self):
        return f"{self.sector}"

class location(db.Model):
    """
    Location db model to store location choice
    """
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(10), nullable=False)
    location_backref = db.relationship('job_post', backref='location_ref', lazy=True)
    def __repr__(self):
        return f"{self.city}"
