from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required
from my_app.parent.models import Parent, ParentForm, AddressForm
from my_app.child.models import Child, ChildForm


parent_blueprint = Blueprint("parent", __name__)


# context_processor to combine persona's first_name and last_name
@parent_blueprint.context_processor
def full_name_processor():
	def full_name(name):
		return "{0} {1}".format(name["first_name"], name["last_name"])

	return {"full_name": full_name}


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


@parent_blueprint.route("/edit-parent/<id>", methods=["GET", "POST"])
@login_required
def edit_parent(id):
	child = Child.objects.get(id=id)
	parent = Parent.objects.get(id=child.parent.id)

	form = ParentForm(meta={'csrf': False})

	if request.method == "POST":
		# parent.update(
		# 	first_name = form.first_name.data,
		# 	last_name = form.last_name.data,
		# 	phone = form.phone.data,
		# 	address = form.address.data
		# )

		print(form.address.data)
		
		address = []

		for address_line in form.address.data:
			print(address_line)
			new_address_line = AddressForm(**address_line)

			# Add to parent
			address.append(new_address_line)
			# parent.address.append(new_address_line)

		print(address)

		return redirect(url_for("child.view_child", id=id))

	return render_template("edit-parent.html", form=form, child=child, parent=parent)

# @parent_blueprint.route("/delete-parent/<id>")
# @login_required
# def delete_parent(id):
# 	parent = Parent.objects.get_or_404(id=id)

# 	parent.delete()

# 	return redirect(url_for("child.dashboard"))