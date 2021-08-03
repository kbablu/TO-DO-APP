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

# Finally, create the necessary database tables
db.create_all()