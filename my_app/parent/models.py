from my_app import db
from bson import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


# mongo document schema for Child
class Parent(db.Document):
	first_name = db.StringField(maxlength=255, required=True)
	last_name = db.StringField(maxlength=255, required=True)
	phone = db.StringField(maxlength=255)
	address = db.StringField(maxlength=255)

	def __repr__(self):
		return "<Parent %r>" % self._id

# form schema to add a child
class ParentForm(FlaskForm):
	first_name = StringField("First name", validators=[InputRequired()])
	last_name = StringField("Last name", validators=[InputRequired()])
	phone = StringField("Phone")
	address = StringField("Address")