#!/usr/bin/python3
""" A script that starts a Flask web application """
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page: (inside the tag BODY)"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page: (inside the tag BODY)"""
    state = None
    for value in storage.all("State").values():
        if value.id == id:
            state = value
            break
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
