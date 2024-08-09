#!/usr/bin/python3
"""how we start flask application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """greeting"""
    return "Hello HBNB!"


"""application will be listening here"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
