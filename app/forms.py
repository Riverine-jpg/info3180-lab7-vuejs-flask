from wtforms.validators import DataRequired, Email
from flask import Flask
from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    desc = TextAreaField("Description", validators=[DataRequired()],name="Description")
    photo = FileField(validators=[ FileAllowed(['png', 'jpg','jpeg'], "wrong format!")])
    submit = SubmitField('Upload')