

from flask import flask

app = flask (__name__)

app.run(debag=true)
@app.route('/')
def hello():
    return "<h1> this is my first page </h1>"