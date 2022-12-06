#!/usr/bin/python3
"""First flask module for HBNB"""


from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_app_close(self):
    "Closses session"
    storage.close()


@app.route('/states_list')
def states_list():
    """Returns a HTML with states list"""
    state_dict = storage.all(State)
    list = []
    for state in state_dict.values():
        list.append(state)
    return render_template('7-states_list.html', sorted_list=list)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
