from jobseek import db
from datetime import datetime

# create employer user db model 
class employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    job_posts = db.relationship('job_post', backref='author', lazy=True)
    # string to return in shell when employer model called
    def __repr__(self):
        return f"User: {self.companyName}"

# create job_post db model
class job_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(60), nullable=False)
    sector = db.Column(db.String(60), nullable=False)
    location = db.Column(db.String(60), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    role_sum = db.Column(db.Text, nullable=False)
    resp = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    emp_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False )
    # string to return in shell when job_post model called
    def __repr__(self):
        return f"Job Post: {self.date_posted}, {self.title}"

