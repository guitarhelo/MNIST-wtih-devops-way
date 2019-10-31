import os
from random import randint

import flask
from flask import Flask, request, render_template, send_from_directory   #framwork for web

__author__ = 'manwei'

app = Flask(__name__)

@app.route("/")
def index():
    return ("hello world")

@app.route("/hello")
def hello():
    return ("hello who?")

@app.route("/hello/<string:name>/")
def helloName(name):
    return "Welcome " + name

@app.route("/quote/<string:name>/")
def quote(name):

    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
            "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
            "'To understand recursion you must first understand recursion..' -- Unknown",
            "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
            "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
            "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]

    return render_template(
        'test.html',**locals())

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4001))
    app.run(host='0.0.0.0', port=port, debug=True)