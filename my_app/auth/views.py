from flask import request, render_template, redirect, url_for, Blueprint, g
from flask_login import current_user, login_user, logout_user, login_required
from my_app import login_manager
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
	if current_user.is_authenticated:
		return redirect(url_for("child.dashboard"))

	form = RegistrationForm(meta={'csrf': False})

	if form.validate_on_submit():
		try:
			existing_user = User.objects.get(username=form.username.data)

			if existing_user:
				print("That username is already taken. Please try another one.")
			
			return render_template("register.html", form=form)

		except User.DoesNotExist:
			pass

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
		
		try:
			existing_user = User.objects.get(username=username)
			
			if not (existing_user and existing_user.check_password(password)):
				print("Invalid username or password. Please try again.")
				
				return render_template("login.html", form=form)

			login_user(existing_user)

			return redirect(url_for("child.dashboard"))

		except User.DoesNotExist:
			pass
		
	
	return render_template("login.html", form=form)


@auth_blueprint.route("/logout")
@login_required
def logout():
	logout_user()

	return redirect(url_for("auth.login"))