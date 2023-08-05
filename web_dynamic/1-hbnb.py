#!/usr/bin/python3
""" Replace the route 0-hbnb with 1-hbnb """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ a Flask decorator  to remove the current SQLAlchemy Session.
    """
    storage.close()


@app.route('/1-hbnb', strict_slashes=False)
"""This is a Flask route decorator."""
def hbnb():
    """ function that handles the '/1-hbnb' route."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('1-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places, cache_id=uuid.uuid4())


if __name__ == "__main__":
    "This is the main script."
    app.run(host='0.0.0.0', port=5000)
