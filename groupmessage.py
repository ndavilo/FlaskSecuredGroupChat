from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import secrets
app = Flask(__name__)
app.config['SECRET_KEY'] = '319abf33964951556c043d22f04a4d6b'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	key=secrets.token_hex(16)
	return render_template('home.html', key=key)

@app.route("/about")
def room():
	return "<title> About </title>"

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)