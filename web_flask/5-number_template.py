#!/usr/bin/python3
"""module with hello world"""
from flask import Flask, render_template


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
def number(n):
    """only id number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """number template"""
    number = "Number: {}".format(n)
    return render_template('5-number.html', number=number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
