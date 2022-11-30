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
    return 'C {}'.format(text)


@app.route('/python', defaults={'text': "is_cool"}, strict_slashes=False)
@app.route('/python/<text>')
def python(text):
    """capture variable python"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number(text):
    """only id number"""
    return 'Python {}'.format(n)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
