from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Task Name", [validators.Length(min=2)])
    # field that allows the user to specify a task as done or not
    done = BooleanField("Done")

    class Meta:
        csrf = False


