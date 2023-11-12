from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from datetime import datetime, timedelta
from cachetools import TTLCache
from bestpark import combinator
import json

app = Flask(__name__)
CORS(app)

# Using TTLCache as an equivalent for NodeCache with a TTL of 1 hour
api_cache = TTLCache(maxsize=1000, ttl=3600)

# Importing config values from a separate module
from config import config

# @app.route('/getToken', methods=['GET'])
def get_token():
    # url to produce token based on appId and hashToken
    response_headers = {'Access-Control-Allow-Origin': '*'}

    # get from .env variables
    # appId = os.environ.get('APP_ID')  # req.args.get('appId')
    # hashToken = os.environ.get('HASH_TOKEN')

    app_id = config['appId']
    hash_token = config['hashToken']

    if app_id in api_cache:
        # Serve response from cache
        return jsonify(api_cache[app_id]), 200, response_headers
    else:
        # create server request
        headers = {
            'content-type': 'application/json',
            'Accept': 'application/json',
        }

        params = {
            'appId': app_id,
            'hashToken': hash_token,
        }

        try:
            response = requests.get(config['authTokenUrl'], params=params, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(err)
            return jsonify({'error': 'error fetching token'}), 500, response_headers

        if response.status_code == 200:
            one_hour = 60 * 60  # One hour in seconds
            exp = (datetime.utcnow() + timedelta(seconds=one_hour)).timestamp()

            payload = {
                'token': response.json()['result']['token'],
                'exp': exp,  # in seconds
            }

            # Set value for the same appId to serve future requests efficiently
            api_cache[app_id] = payload
            return jsonify(payload), 200, response_headers
        



@app.route('/checkConfig', methods=['GET'])
def check_config():
    exists = all(key in config for key in ('appId', 'hashToken', 'authTokenUrl'))
    payload = {
        'exists': exists,
    }
    return jsonify(payload), 200, {'Access-Control-Allow-Origin': '*'}


# do logic in get street parking
# query our own api from the front end
# return jsonify object 
@app.route('/getStreetParking', methods=['GET'])
def get_street_parking():
    # getting bearer token
    get_token()
    token = api_cache[config['appId']]['token']

    # response_headers = {'Access-Control-Allow-Origin': '*'}
    lat = request.args.get('lat')
    long = request.args.get('long')

    # headers = {
    #         'content-type': 'application/json',
    #         'Accept': 'application/json',
    #     }

    # params = {
    #         'lat': lat,
    #         'long': long,
    #     }
    
    #response = requests.request("GET", url, headers=headers, params=params)

    #print(response.json()) for testing
    
    dict = combinator(lat,long,token)
    return json.dumps(dict, indent=4)
    #return jsonify(response.json()), 200, {'Access-Control-Allow-Origin': '*'}
    # return json object for coord

if __name__ == '__main__':
    port = 3000
    app.run(port=port)
    print(f'Open the URL: http://localhost:{port} in your browser')



