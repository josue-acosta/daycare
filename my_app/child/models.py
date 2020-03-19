from my_app import db
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired

# mongo document schema for Child
class Child(db.Document):
	first_name = db.StringField(maxlength=255, required=True)
	last_name = db.StringField(maxlength=255, required=True)
	birthday = db.DateTimeField(required=True)
	age_group = db.DecimalField()

	def __repr__(self):
		return "<Children %r>" % self.id

# form schema to add a child
class ChildForm(FlaskForm):
	first_name = StringField("First name", validators=[InputRequired()])
	last_name = StringField("Last name", validators=[InputRequired()])
	birthday = DateField("Birthday", validators=[InputRequired()], format='%Y-%m-%d')