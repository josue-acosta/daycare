from my_app import db
from flask_wtf import FlaskForm
from wtforms import StringField, FormField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired
from my_app.parent.models import Parent, ParentForm

# mongo document schema for Child
class Child(db.Document):
	first_name = db.StringField(maxlength=255, required=True)
	last_name = db.StringField(maxlength=255, required=True)
	birthday = db.DateTimeField()
	age_group = db.DecimalField()
	parent = db.ReferenceField(Parent)

	def __repr__(self):
		return "<Children %r>" % self.id

# form schema to add a child
class ChildForm(FlaskForm):
	first_name = StringField("First name", validators=[InputRequired()])
	last_name = StringField("Last name", validators=[InputRequired()])
	birthday = DateField("Birthday", format='%Y-%m-%d')
	parent = FormField(ParentForm)