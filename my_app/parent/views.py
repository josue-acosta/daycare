from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required
from my_app.parent.models import Parent, ParentForm
from my_app.child.models import Child, ChildForm


parent_blueprint = Blueprint("parent", __name__)
