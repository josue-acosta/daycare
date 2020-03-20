from my_app import db
from bson import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


# mongo document schema for Child
class Parent(db.EmbeddedDocument):
	_id = db.ObjectIdField(default=ObjectId)
	first_name = db.StringField(maxlength=255, required=True)
	last_name = db.StringField(maxlength=255, required=True)

	def __repr__(self):
		return "<Parent %r>" % self.id

# form schema to add a child
class ParentForm(FlaskForm):
	first_name = StringField("First name", validators=[InputRequired()])
	last_name = StringField("Last name", validators=[InputRequired()])