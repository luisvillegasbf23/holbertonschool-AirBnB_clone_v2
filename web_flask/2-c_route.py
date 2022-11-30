#!/usr/bin/python3
"""module with hello world"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ first end point """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ second  end point """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """capture variable"""
    text = text.replace("_", " ")
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
