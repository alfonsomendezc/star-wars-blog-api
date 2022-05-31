"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Response
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Planet, Person, FavoritePlanet
import requests
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def handle_hello():
    users = User.query.all()
    users_serialize = list(map(lambda user: user.serialize(), users))
    print(users)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": users_serialize
    }

    return jsonify(response_body), 200

@app.route('/user/favorites', methods=['GET'])
def handle_favorites():
    return "Favorites", 200

@app.route('/people', methods=['GET'])
def handle_people():

    response = requests.get("https://www.swapi.tech/api/people/")
    response_decoded = response.json()
    people = People.query.all()
    if len(people) == 0:
        for people in response_decoded['results']:
            response_one_people = requests.get(people["url"])
            response_one_people_decoded = response_one_people.json()
            response_one_people_decoded['result']
            one_people = People(**response_one_people_decoded['result']['properties'],_id=response_one_people_decoded['result']['_id'],uid=response_one_people_decoded['result']['uid'])
            db.session.add(one_people)
        db.session.commit()

    return response_decoded, 200


# @app.route('/people/<int:people_id>', methods=['GET'])
# def handle_person(people_id):

#     response = requests.get(f"https://www.swapi.tech/api/people/{people_id}")
#     return response.json(), 200

@app.route('/planets', methods=['GET'])
def handle_planet():

    response = requests.get("https://www.swapi.tech/api/planets/")
    response_decoded = response.json()
    planets = Planet.query.all()
    if len(planets) == 0:
        for planet in response_decoded['results']:
            response_one_planet = requests.get(planet["url"])
            response_one_planet_decoded = response_one_planet.json()
            response_one_planet_decoded['result']
            one_planet = Planet(**response_one_planet_decoded['result']['properties'],_id=response_one_planet_decoded['result']['_id'],uid=response_one_planet_decoded['result']['uid'])
            db.session.add(one_planet)
        db.session.commit()

    return response_decoded, 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def favorite_planet(planet_id):
    user = list(User.query.filter_by(is_active=True))
    planet = list(Planet.query.filter_by(uid=planet_id))
    if len(user) > 0 and len(planet) > 0:
        my_favorite_planet = FavoritePlanet(user[0].id, planet[0].id)
        db.session.add(my_favorite_planet)
        db.session.commit()
    return {"msg":f"Creado favorito con el id: {user[0].id} y el planeta de id: {planet[0].id}"}


# @app.route('/planets/<int:planets_id>', methods=['GET'])
# def handle_planet():

#     response = requests.get(f"https://www.swapi.tech/api/planets/{planets_id}")
#     return response.json(), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
