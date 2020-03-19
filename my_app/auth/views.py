from flask import request, render_template, redirect, url_for, session, Blueprint, g
from flask_login import current_user, login_user, logout_user, login_required
from my_app import app, db, login_manager
from my_app.auth.models import User, RegistrationForm, LoginForm


auth_blueprint = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(id):
	return User.objects.get_or_404(id=id)


@auth_blueprint.before_request
def get_current_user():
	g.user = current_user


@auth_blueprint.route("/register", methods=["POST", "GET"])
def register():
	if session.get("username"):
		return redirect(url_for("child.dashboard"))

	form = RegistrationForm(meta={'csrf': False})

	if form.validate_on_submit():

		user = User (
			username = form.username.data,
			password = form.password.data
		)

		user.save()

		return redirect(url_for("auth.login"))

	return render_template("register.html", form=form)


@auth_blueprint.route("/", methods=["GET", "POST"])
def login():
	form = LoginForm(meta={'csrf': False})

	if current_user.is_authenticated:
		print("user is already authenticated")

	if form.validate_on_submit():

		username = request.form.get("username")
		password = request.form.get("password")		
		
		existing_username = User.objects.get_or_404(username=username)	

		if not (existing_username["username"] and existing_username["password"]):
			return render_template("login.html", form=form)

		login_user(existing_username)

		return redirect(url_for("child.dashboard"))
	
	return render_template("login.html", form=form)


@auth_blueprint.route("/logout")
@login_required
def logout():
	logout_user()

	return redirect(url_for("auth.login"))