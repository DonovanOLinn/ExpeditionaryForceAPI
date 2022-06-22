from os import stat
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash
from datetime import datetime


db = SQLAlchemy()


class Species(db.Model):
    species_name = db.Column(db.String, primary_key=True)
    appearence = db.Column(db.String)
    patron = db.Column(db.String)
    client = db.Column(db.String)
    tech_level = db.Column(db.String)
    nickname = db.Column(db.String)
    coalition = db.Column(db.String)
    image = db.Column(db.String)


    def __init__(self, appearence, patron, client, tech_level, nickname, coalition, image):
        self.appearence = appearence
        self.patron = patron
        self.client = client
        self.tech_level = tech_level
        self.nickname = nickname
        self.coalition = coalition
        self.image = image

    def to_dict(self):
        return {
            'species_name': self.species_name,
            'appearence': self.appearence,
            'patron': self.patron,
            'client': self.client,
            'tech_level': self.tech_level,
            'nickname': self.nickname,
            'coalition': self.coalition,
            'image': self.image
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])

class Books(db.Model):
    bookname = db.Column(db.String, primary_key=True)
    author = db.Column(db.String)
    narrator = db.Column(db.String)
    release = db.Column(db.String)
    publisher = db.Column(db.String)
    runtime = db.Column(db.String)
    previous = db.Column(db.String)
    next = db.Column(db.String)
    authorsummary = db.Column(db.String)
    image = db.Column(db.String)

    def __init__(self, author, narrator, release, publisher, runtime, previous, next, authorsummary, image):
        self.author = author,
        self.narrator = narrator,
        self.release = release,
        self.publisher = publisher,
        self.runtime = runtime,
        self.previous = previous,
        self.next = next,
        self.authorsummary = authorsummary,
        self.image = image

    def to_dict(self):
        return {
            'bookname': self.bookname,
            'author': self.author,
            'narrator': self.narrator,
            'release': self.release,
            'publisher': self.publisher,
            'runtime': self.runtime,
            'previous': self.previous,
            'next': self.next,
            'authorsummary': self.authorsummary,
            'image': self.image
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])


class Characters(db.Model):
    name = db.Column(db.String, primary_key=True)
    alias = db.Column(db.String)
    rank = db.Column(db.String)
    affiliation = db.Column(db.String)
    relationship = db.Column(db.String)
    species_name = db.Column(db.String, db.ForeignKey('Species.species_name'))
    sex = db.Column(db.String)
    status = db.Column(db.String)
    first_appearence = db.Column(db.String)
    last_known_location = db.Column(db.String)

    def __init__(self, name, alias, rank, affiliation, relationship, species_name, sex, status, first_appearence, last_known_location):
        self.name = name,
        self.alias = alias,
        self.rank = rank,
        self.affiliation = affiliation,
        self.relationship = relationship,
        self.species_name = species_name,
        self.sex = sex,
        self.status = status,
        self.first_appearence = first_appearence,
        self.last_known_location = last_known_location

    def to_dict(self):
        return {
            'name': self.name,
            'alias': self.alias,
            'rank': self.rank,
            'affiliation': self.affiliation,
            'relationship': self.relationship,
            'species_name': self.species_name,
            'sex': self.sex,
            'status': self.status,
            'first_appearence': self.first_appearence,
            'last_known_location': self.last_known_location
        }
    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])

class Planets(db.Model):
    name = db.Column(db.String, primary_key=True)
    nickname = db.Column(db.String)
    species_name = db.Column(db.String)
    nativespecies = db.Column(db.String)
    planetdata = db.Column(db.String)

    def __init__(self, nickname, species_name, nativespecies, planetdata):
        #self.name = name,
        self.nickname = nickname,
        self.species_name = species_name,
        self.nativespecies = nativespecies,
        self.planetdata = planetdata

    def to_dict(self):
        return {
            'name': self.name,
            'nickname': self.nickname,
            'species_name': self.species_name,
            'nativespecies': self.nativespecies,
            'planetdata': self.planetdata
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])

class Ships(db.Model):
    shipname = db.Column(db.String, primary_key=True)
    shiptype = db.Column(db.String)
    species_name = db.Column(db.String, db.ForeignKey('Species.species_name'))
    controlai = db.Column(db.String)
    armament = db.Column(db.String)
    status = db.Column(db.String)
    description = db.Column(db.String)

    def __init__(self, shiptype, species_name, controlai, armament, status, description):
        self.shiptype = shiptype,
        self.species_name = species_name,
        self.controlai = controlai,
        self.armament = armament,
        self.status = status,
        self.description = description

    def to_dict(self):
        return {
            'shipname': self.shipname,
            'shiptype': self.shiptype,
            'controlai': self.controlai,
            'armament': self.armament,
            'status': self.status,
            'description': self.description
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])