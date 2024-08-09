#!/usr/bin/python3
"""flask app with double tabs"""

from flask import Flask

app = Flask(__name__)

"""return hello HBNB"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


"""return HBNB"""


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


"""web app listening on 0.0.0.0, port 5000"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
