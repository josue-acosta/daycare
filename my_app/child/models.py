from my_app import db
from flask_wtf import FlaskForm
from wtforms import StringField, FormField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired
from my_app.parent.models import Parent, ParentForm
from datetime import date, datetime

# mongo document schema for Child
class Child(db.Document):
	first_name = db.StringField(maxlength=255, required=True)
	last_name = db.StringField(maxlength=255, required=True)
	birthday = db.DateTimeField()
	age_group = db.IntField()
	parent = db.ReferenceField(Parent)

	def calculate_age_group(self, birthday):
		today = date.today()
		months = ((today.year - birthday.year) * 12 ) + birthday.month
		age_group = None
		
		if months >= 36:
			age_group = 4
		elif months >= 12 and months < 36:
			age_group = 3
		elif months >= 6 and months < 12:
			age_group = 2
		elif months > 0 and months < 6:
			age_group = 1
		else:
			return "Could not calculate age group"

		return age_group

	def __repr__(self):
		return "<Children %r>" % self.id

# form schema to add a child
class ChildForm(FlaskForm):
	first_name = StringField("First name", validators=[InputRequired()])
	last_name = StringField("Last name", validators=[InputRequired()])
	birthday = DateField("Birthday", format='%Y-%m-%d')
	parent = FormField(ParentForm)


def group_age_group(children):
	age_group = {
		"age_group_1_count": len([child for child in children if child.age_group == 1]),
		"age_group_2_count": len([child for child in children if child.age_group == 2]),
		"age_group_3_count": len([child for child in children if child.age_group == 3]),
		"age_group_4_count": len([child for child in children if child.age_group == 4])
	}	

	return age_group