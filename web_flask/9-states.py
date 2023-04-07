#!/usr/bin/python3
""" script that starts a Flask web application """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    storage.close()


@app.route("/states", strict_slashes=False)
def listStates():
    states = storage.all(State)
    cities = storage.all(City)

    return render_template("9-states.html", states=states, cities=cities)


@app.route("/states/<id>", strict_slashes=False)
def listStateCities(id):
    citiesList = storage.all(City)
    statesList = storage.all(State)
    for state in statesList.values():
        print(str(state.id) + " ===" + str(id))
        if str(state.id) == str(id):
            return render_template("9-states.html", states=state, cities=citiesList)
    return render_template("9-states.html", cities=citiesList)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
