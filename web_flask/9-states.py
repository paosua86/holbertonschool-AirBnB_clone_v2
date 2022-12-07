#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""


from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def l_states():
    """ List all states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """ List a specific state with it's cities """
    flag = 0
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            flag = 1
            break
    return render_template('9-states.html', state=state, flag=flag)


@app.teardown_appcontext
def close(db):
    """ Close the current sessions after each request """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
