#!/usr/bin/python3

"""add flixable text"""

from flask import Flask
app = Flask(__name__)


"""return hello HBNB"""


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


"""return HBNB """


@app.route('/hbnb', strict_slashes=False)
def showHBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display “C ” followed by the value of the text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
