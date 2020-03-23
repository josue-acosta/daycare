from my_app import db
from bson import ObjectId
from flask_wtf import FlaskForm
from wtforms import Form, StringField, FormField, FieldList
from wtforms.validators import InputRequired


# mongo document schema for Parent
class Parent(db.Document):
	first_name = db.StringField(maxlength=255, required=True)
	last_name = db.StringField(maxlength=255, required=True)
	phone = db.StringField(maxlength=255)
	address = db.StringField(maxlength=255)

	def __repr__(self):
		return "<Parent %r>" % self._id


# sub form schema of address for parent
class AddressForm(Form):
	address_line = StringField("Address")


# form schema to add a parent
class ParentForm(FlaskForm):
	first_name = StringField("First name", validators=[InputRequired()])
	last_name = StringField("Last name", validators=[InputRequired()])
	phone = StringField("Phone")
	address = FieldList(
		FormField(AddressForm), min_entries=1, max_entries=4
	)

