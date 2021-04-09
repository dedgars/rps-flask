from flask import render_template, request, redirect, url_for

from main import app
from main.forms import RPSbuttons
import random

from main import db
from datetime import datetime


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


#
# def button_play(element):
#     elements = [['ROCK', 0], ['PAPER', 1], ['SCISSORS', 2]]
#     form = RPSbuttons()
#     if form.validate_on_submit():
#         if element in request.form:
#             played = element
#             computer_played = random.choice(elements)[0]
#             computer_played_value = random.choice(elements)[1]
#             winner = get_winner(played[1], computer_played_value)


@app.route('/play', methods=['GET', 'POST'])
def play():
    vs = 'vs'
    form = RPSbuttons()
    elements = {'ROCK': 0, 'PAPER': 1, 'SCISSORS': 2}
    if request.method == "POST":
        if request.form['submit_button'] in elements.keys():
            played = request.form['submit_button']
            c_played = random.choice([k for k in elements.keys()])
            played_value = elements[played]
            c_played_value = elements[c_played]
            result = get_winner(played_value, c_played_value)
            return render_template('play.html', form=form, played=played, c_played=c_played, result=result, vs=vs)
    elif request.method == "GET":
        return render_template('play.html', form=form)


def get_winner(a, b):
    if (a + 1) % 3 == b:
        return 'Computer wins'
    elif a == b:
        return 'Draw'
    else:
        return 'Player wins'



