from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required
from my_app.child.models import Child, ChildForm
from my_app.parent.models import Parent, ParentForm

child_blueprint = Blueprint("child", __name__)

# context_processor to combine child's first_name and last_name
@child_blueprint.context_processor
def full_name_processor():
	def full_name(child):
		return "{0} {1}".format(child["first_name"], child["last_name"])

	return {"full_name": full_name}


@child_blueprint.route("/dashboard")
@login_required
def dashboard():
	children = Child.objects.all()

	return render_template("dashboard.html", children=children)


@child_blueprint.route("/add", methods=["GET", "POST"])
@login_required
def add():
	form = ChildForm(meta={'csrf': False})

	if request.method == "POST":
		parent = Parent (
			first_name = form.parent.first_name.data,
			last_name = form.parent.last_name.data
		)

		child = Child (
			first_name = form.first_name.data,
			last_name = form.last_name.data,
			birthday = form.birthday.data,
			parent = [parent]
		)

		child.save()

		return redirect(url_for("child.dashboard"))
	
	return render_template("add-child.html", form=form)


@child_blueprint.route("/view/<id>")
@login_required
def view_child(id):
	child = Child.objects.get_or_404(id=id)

	return render_template("view-child.html", child=child)


@child_blueprint.route("/edit/<id>", methods=["GET", "POST"])
@login_required
def edit_child(id):
	child = Child.objects.get_or_404(id=id)
	form = ChildForm(meta={'csrf': False})

	if request.method == "POST":
		child.update(
			first_name = form.first_name.data,
			last_name = form.last_name.data,
			birthday = form.birthday.data
		)

		return redirect(url_for("child.view_child", id=id))

	return render_template("edit-child.html", child=child, form=form)


@child_blueprint.route("/delete/<id>")
@login_required
def delete_child(id):
	child = Child.objects.get_or_404(id=id)

	child.delete()

	return redirect(url_for("child.dashboard"))