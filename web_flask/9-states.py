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


@app.route('/states_list')
@app.route('/states_list/<id>')
def states_list(id=None):
    """Returns a HTML with states list"""
    state_list = storage.all(State).values()
    if not id:
        return render_template('9-states.html', sorted_list=state_list, status=1)
    for state in state_list:
        if state.id == id:
            return render_template('9-states.html', sorted_list=[state], status=2)
    return render_template('9-states.html', sorted_list=None, status=0)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port="5000")
