# Introducing Flask
from flask import Flask
app = Flask(__name__)

# Introducing SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


# Use an SQLite database named tasks.db. Three slashes
# says the file is located with the files in this application
# in the same place
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
# Ask SQLAlchemy to print all SQL queries
app.config["SQLALCHEMY_ECHO"] = True
# Suppress the warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Create a db object that is used to process the database
db = SQLAlchemy(app)

# Read the contents of the application file views from the folder
from application import views

from application.tasks import models
from application.tasks import views

from application.auth import models
from application.auth import views

# logging
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Finally, create the necessary database tables
db.create_all()