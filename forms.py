from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AddTaskForm(FlaskForm):
    task = StringField('Task Title', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Add Task')