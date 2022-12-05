#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run()
