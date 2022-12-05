#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """/: display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """/hbnb: display “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>')
def C_is_fun(text):
    """display “C ” followed by the value of the
    text variable (replace underscore _ symbols with a space”"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """display “Python ”, followed by the value of
    the text variable (replace underscore _ symbols with a space ”"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """ display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return str(n) + ' is a number'


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
