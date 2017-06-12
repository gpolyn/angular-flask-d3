import traceback
import json
from bson.json_util import dumps
from flask import Flask, jsonify, request, Response
from flask_jwt import JWT, jwt_required, current_identity
from pymongo import MongoClient
from gevent.wsgi import WSGIServer
client = MongoClient('db')
db = client.usda
from .factory import create_app
import logging
from .app_utils import html_codes, token_login
logger = logging.getLogger(__name__)
app = create_app()
 
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
 
    def __str__(self):
        return "User(id='%s')" % self.id
 
user = User(1, 'user', 'password')
 
 
def authenticate(username, password):
    if username == user.username and password == user.password:
        return user
 
def identity(payload):
    return user
 
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
 
jwt = JWT(app, authenticate, identity)
 
 
# send CORS headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response
 
 
@app.route('/unprotected')
def unprotected():
    return jsonify({
        'message': 'This is an unprotected resource.'
    })
 
 
@app.route('/protected')
@jwt_required()
def protected():
    return jsonify({
        'message': 'This is a protected resource.',
        'current_identity': str(current_identity)
    })

@app.route('/api/getdata', methods=['POST'])
# @auth_token_required
def get_data():
    """Get dummy data returned from the server."""
    logger.info('Data served from jwt_server')
    a = db.pie.find_one()
    json_response = dumps(a['data'])
    # data = {'Heroes': ['Hero1', 'Hero2', 'Hero3']}
    # json_response = json.dumps(data)
    return Response(json_response,
                    status=html_codes.HTTP_OK_BASIC,
                    mimetype='application/json')

def main():
    """Main entry point of the app."""
    try:
        http_server = WSGIServer(('0.0.0.0', 8080),
                                 app,
                                 log=logging,
                                 error_log=logging)
        http_server.serve_forever()
    except Exception as exc:
        logger.error(exc.message)
        logger.exception(traceback.format_exc())
    finally:
        # Do something here
        pass
