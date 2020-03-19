from my_app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, EqualTo, DataRequired


# mongo document schema for Child
class User(db.Document):
	username = db.StringField(maxlength=255, required=True)
	password = db.StringField(maxlength=255, required=True)

	# def __init__(self, username, password):
	# 	self.username = username
	# 	self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)


# form schema to register
class RegistrationForm(FlaskForm):
	username = TextField("Username", [InputRequired()])
	password = PasswordField("Password", [
    	InputRequired(),
    	EqualTo("confirm", message="Passwords must match")
    ])
	confirm = PasswordField("Confim Password", [InputRequired()])


# form schema to login
class LoginForm(FlaskForm):
	username = TextField("Username", [InputRequired()])
	password = PasswordField("Password", [InputRequired()])