#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""


from models import storage
from models.state import State
from flask import Flask, render_template
from os import getenv
app = Flask(__name__)
environ = getenv('HBNB_TYPE_STORAGE')

@app.teardown_appcontext
def teardown_app_close(self):
    "Closses session"
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """Returns a HTML with states list"""
    state_list = storage.all(State).values()
    return render_template('8-cities_by_states.html', sorted_list=state_list)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
