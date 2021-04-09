from flask_wtf import FlaskForm
from wtforms import SubmitField


class RPSbuttons(FlaskForm):
    rock = SubmitField(label='Rock')
    paper = SubmitField(label='Paper')
    scissors = SubmitField(label='Scissors')