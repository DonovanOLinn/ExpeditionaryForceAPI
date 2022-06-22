from flask import json, Blueprint, jsonify, request, redirect, url_for, render_template
from app.models import Species, Books, Characters, Planets, Ships, db
import pandas as pd
api = Blueprint('api', __name__, template_folder='api_templates', url_prefix='/api')

@api.route('/test', methods=['GET'])
def test():
    x = 'start'
    print(x)
    return render_template('api_base.html'), 200

@api.route('/Species', methods=['GET'])
def getSpecies():
    print('start')
    species = Species.query.all()
    species = [sp.to_dict() for sp in species]
    
    return jsonify(species), 200

@api.route('/Species/<string:name>', methods=['GET'])
def getSpeciesspecific(name):
    print('start')
    species = Species.query.filter(Species.species_name == name).all()
    species = [sp.to_dict() for sp in species]
    
    return jsonify(species), 200

@api.route('/Books', methods=['GET'])
def getBooks():
    print('start')
    books = Books.query.all()
    books = [bs.to_dict() for bs in books]
    
    return jsonify(books), 200

@api.route('/Characters', methods=['GET'])
def getCharacters():
    print('start')
    characters = Characters.query.all()
    characters = [ch.to_dict() for ch in characters]

    return jsonify(characters), 200

@api.route('/Planets', methods=['GET'])
def getPlanets():
    print('start')
    planets = Planets.query.all()
    planets = [pl.to_dict() for pl in planets]
    return jsonify(planets), 200

@api.route('/Ships', methods=['GET'])
def getShips():
    print('start')
    ships = Ships.query.all()
    ships = [sh.to_dict() for sh in ships]
    return jsonify(ships), 200

@api.route('Species/all/<string:name>', methods=['GET'])
def getspecificspecies(name):
    print('start')
    my_filter = Characters.query.filter(Characters.species_name == name).all()
    my_ships = Ships.query.filter(Ships.species_name == name).all()
    my_species = Species.query.filter(Species.species_name == name).all()
    my_planets = Planets.query.filter(Planets.species_name == name).all()
    #my_filter = Species.query.all()
    my_filter = [sp.to_dict() for sp in my_filter]
    my_ships = [sh.to_dict() for sh in my_ships]
    my_species = [ch.to_dict() for ch in my_species]
    my_planets = [pl.to_dict() for pl in my_planets]
    return jsonify(my_filter, my_ships, my_species, my_planets), 200
    #return render_template('api_base.html'), 200


@api.route('character/<string:name>', methods=['GET'])
def getspecificcharacter(name):
    print('start')
    my_char = Characters.query.filter(Characters.name == name).all()
    my_char = [ch.to_dict() for ch in my_char]
    return jsonify(my_char), 200