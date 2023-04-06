#!/usr/bin/python3
"""A script that starts a Flask web application with storage"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    states_sorted = sorted(states, key, states: states.name)
    cities = storage.all(City).values()
    cities_sorted = sorted(cities, key, cities: cities.name)
    return render_template('8-cities_by_states.html',
                           states=states_sorted, cities=cities_sorted)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
