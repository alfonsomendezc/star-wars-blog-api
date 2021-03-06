from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_planets = db.relationship('FavoritePlanets', lazy = True)
    favorite_people = db.relationship('FavoritePeople', lazy = True)

    def __repr__(self):
        return f"Active Profile's username: {self.email}"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    mass = db.Column(db.String(120), unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    skin_color = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)
    homeworld = db.Column(db.String(120), unique=False)
    created = db.Column(db.String(120), nullable=False)
    edited = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    _id = db.Column(db.String(120), unique=True, nullable=True)
    uid = db.Column(db.String(120), unique=True, nullable=True)

    def __init__(self, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, created, edited, url, homeworld=None, _id=None, uid=None):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.created = created
        self.edited = edited
        self.url = url
        self._id = _id
        self.uid = uid


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_planet= db.relationship('FavoritePlanets', lazy = True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(120), nullable=False)
    rotation_period = db.Column(db.String(120), nullable=False)
    orbital_period = db.Column(db.String(120), nullable=False)
    gravity = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120), nullable=False)
    terrain = db.Column(db.String(120), nullable=False)
    surface_water = db.Column(db.String(120), nullable=False)
    created = db.Column(db.String(120), nullable=False)
    edited = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    _id = db.Column(db.String(120), unique=True, nullable=True)
    uid = db.Column(db.String(120), unique=True, nullable=True)

    def __init__(self, name, diameter, rotation_period, orbital_period, gravity, population, climate, terrain, surface_water, created, edited, url, _id=None, uid=None):
        self.name = name
        self.diameter = diameter
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.population = population
        self.climate = climate
        self.terrain = terrain
        self.surface_water = surface_water
        self.created = created
        self.edited = edited
        self.url = url
        self._id = _id
        self.uid = uid

class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    
    def __init__(self,user_id,people_id):
        self.user_id = user_id
        self.people_id = people_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }

class FavoritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

    def __init__(self,user_id,planet_id):
        self.user_id = user_id
        self.planet_id = planet_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }