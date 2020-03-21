# Daycare App
This is a CRUD web app built on Flask and the databased is managed by MongoDB.

1. To get started, clone the repo and run this command to install all the dependancies:

	`$ pip install -r requirements.txt`

2. Then run the app:

	`python run.py`

## References found along the way
- https://gist.github.com/nikhilkumarsingh/2c39d161f3d5fe4a40c24d7c9a7a11c3
- https://chrisalbon.com/python/basics/strings_to_datetime/
- https://docs.python.org/3.4/library/datetime.html
- https://flask-user.readthedocs.io/en/latest/mongodb_app.html
- https://stackoverflow.com/questions/16981268/mongoengine-typeerror-init-got-an-unexpected-keyword-argument
- https://www.quora.com/How-do-I-create-and-update-embedded-documents-with-MongoEngine
- https://dev.to/sampart/combining-multiple-forms-in-flask-wtforms-but-validating-independently-cbm
- https://wtforms.readthedocs.io/en/stable/fields.html
- https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters


{
	"_id": "child_00001",
	first_name: "Tuesday",
	last_name: "Grundy",
	birthday: 2020-01-01T00:00:00.000+00:00,
	parent = [
		{ "_id": "parent_00001" }
		{ "_id": "parent_00002" }
	]
}

{
	"_id": "parent_00001",
	first_name: "Solomon",
	last_name: "Grundy",
	children: [
		{ "_id": "child_00001" }
	]
}

{
	"_id": "parent_00002",
	first_name: "Caroline",
	last_name: "Grundy",
	children: [
		{ "_id": "child_00001" }
	]
}