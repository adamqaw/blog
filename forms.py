from flask import Flask, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL
from wtforms.fields import DateField


class NewPost(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    description = StringField("description")
    content = StringField("content")
    author = StringField("author")
    date = StringField("date")
    url = StringField("url")
    img_url = StringField("Blog Image URL")


timespan_choices = ['minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']
sort_choices = ['asc', 'desc']


class StockQuery(FlaskForm):
    stocksTicker = StringField('Ticker', validators=[DataRequired()])
    # multiplier = IntegerField('Multiplier', validators=[DataRequired()])
    # timespan = SelectField('Timespan', choices=timespan_choices, validators=[DataRequired()])
    # _from = DateField('From', validators=[DataRequired()])
    # _to = DateField('To', validators=[DataRequired()])
    # sort = SelectField('Sort', choices=sort_choices, validators=[DataRequired()])
    # limit = IntegerField('Limit')
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit')
