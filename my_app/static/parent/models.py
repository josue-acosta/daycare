from my_app import db
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField
from wtforms.validators import InputRequired, NumberRange

# mongo document schema for Parent
class Parent(db.Document):
	first_name = db.StringField(maxlength=255, required=True)
	last_name = db.StringField(maxlength=255, required=True)

	def __repr__(self):
		return "<Parent %r>" % self.id

# form schema to add a parent
class ParentForm(FlaskForm):
	first_name = StringField("First name", validators=[InputRequired])
	last_name = StringField("Last name", validators=[InputRequired])