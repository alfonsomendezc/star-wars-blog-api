from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_planet = db.relationship('FavoritePlanet', lazy = True)
    favorite_person = db.relationship('FavoritePerson', lazy = True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(120), unique=True, nullable=False)
    mass = db.Column(db.String(120), unique=True, nullable=False)
    hair_color = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.String(120), unique=True, nullable=False)

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(120), unique=True, nullable=False)
    gravity = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120), unique=True, nullable=False)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_person= db.relationship('FavoritePerson', lazy = True)

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_planet= db.relationship('FavoritePlanet', lazy = True)

    def __init__(self):
        pass

class FavoritePerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }

class FavoritePlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }