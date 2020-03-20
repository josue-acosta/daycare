from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required
from my_app.parent.models import Parent, ParentForm
from my_app.child.models import Child


parent_blueprint = Blueprint("parent", __name__)


# @parent_blueprint.route("/dashboard")
# @login_required
# def dashboard():
# 	children = Child.objects.all()

# 	return render_template("dashboard.html", children=children)


# @parent_blueprint.route("/add-parent", methods=["GET", "POST"])
# @login_required
# def add():
# 	form = ParentForm(meta={'csrf': False})

# 	if request.method == "POST":
# 		parent = Parent (
# 			first_name = form.first_name.data,
# 			last_name = form.last_name.data,
# 		)

# 		parent.save()

# 		return redirect(url_for("child.dashboard"))
	
# 	return render_template("add-parent.html", form=form)


# @parent_blueprint.route("/view-parent/<id>")
# @login_required
# def view_parent(id):
# 	child = Child.objects.get_or_404(id=id)

# 	return render_template("view-parent.html", child=child)


# @parent_blueprint.route("/edit/<id>", methods=["GET", "POST"])
# @login_required
# def edit_child(id):
# 	child = Child.objects.get_or_404(id=id)
# 	form = ChildForm(meta={'csrf': False})

# 	if request.method == "POST":
# 		child.update(
# 			first_name = form.first_name.data,
# 			last_name = form.last_name.data,
# 			birthday = form.birthday.data
# 		)

# 		return redirect(url_for("child.view_child", id=id))

# 	return render_template("edit-child.html", child=child, form=form)


# @parent_blueprint.route("/delete-parent/<id>")
# @login_required
# def delete_parent(id):
# 	parent = Parent.objects.get_or_404(id=id)

# 	parent.delete()

# 	return redirect(url_for("child.dashboard"))