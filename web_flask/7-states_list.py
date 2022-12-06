#!/usr/bin/python3
"""First flask module for HBNB"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_close(self):
    "Closses sqlalchemy session"
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Returns a HTML with states list"""
    state_dict = storage.all(State)
    ret_list = []
    for state in state_dict.values():
        ret_list.append(state)
    return render_template('7-states_list.html', st_list=ret_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
