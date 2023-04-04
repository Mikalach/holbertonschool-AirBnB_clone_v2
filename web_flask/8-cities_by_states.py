#!/usr/bin/python3
"""A script that starts a Flask web application with storage"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():

    cities = storage.all(State).values()
    cities_sorted = sorted(cities, key=lambda cities: cities.name)
    return render_template('8-cities_by_states.html', states=cities_sorted)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
