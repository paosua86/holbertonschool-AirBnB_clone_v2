#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """display a HTML page:"""
    states = storage.all(State)
    sorted_states = sorted(states.value(), key=lambda state: state.name)
    return render_template('7-states_list.html', sorted_states=sorted_states)

@app.teardown_appcontext
def storage_close(self):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
