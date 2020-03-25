from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
import ssl


# app config
app = Flask(__name__)
app.config.from_object("configuration.DevelopmentConfig")


# mongo_db config
db = MongoEngine(app)


# authentication config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


# register blueprints
from my_app.child.views import child_blueprint
app.register_blueprint(child_blueprint)

from my_app.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)