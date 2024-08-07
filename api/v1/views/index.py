#!/usr/bin/python3
"""creating flask app and register the blueprint app_views to Flask instance app"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from flask import jsonify

@app_views.route('/status')
def api_status():
    """
    Return a Json response for RESTful API health
    """
    response = {'status': "OK"}
    return jsonify(response)


@app_views.route('/status')
def get_stats():
    """


    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'review': storage.count('Review'),
        'place': storage.count('Place'),
        'state': storage.count('State'),
        'user': storage.count('User'),
    }
    return jsonify(stats)
