import os
from flask import Flask, render_template, url_for, redirect
from forms import registerForm, loginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

def create_app():
    app = Flask(__name__)
    csrf.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)
    

@app.route("/login")
def login():
    form = loginForm()
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)