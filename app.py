import os
from datetime import datetime
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import registerForm, loginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

csrf.init_app(app)


class employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    job_posts = db.relationship('job_post', backref='author', lazy=True)

    def __repr__(self):
        return f"User: {self.companyName}"

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

    def __repr__(self):
        return f"Job Post: {self.date_posted}, {self.title}"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.companyName.data }!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)
    

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)