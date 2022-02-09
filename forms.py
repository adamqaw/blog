from flask import Flask, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL


class NewPost(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    description = StringField("description")
    content = StringField("content")
    author = StringField("author")
    date = StringField("date")
    url = StringField("url")
    img_url = StringField("Blog Image URL")
