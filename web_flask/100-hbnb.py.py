#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place


app = Flask(__name__)


@app.route('//hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    cities = storage.all(City).values()
    places = storage.all(Place).values()
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cities=cities)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)