#!/usr/bin/python3
"""creating flask app and register the blueprint app_views to Flask instance app"""
from flask import jsonify
from api.v1.views import app_views

from flask import jsonify

@app_views.route('/status')
def api_status():
    """
    Defining API status
    """
    response = {'status': "OK"}
    return jsonify(response)

