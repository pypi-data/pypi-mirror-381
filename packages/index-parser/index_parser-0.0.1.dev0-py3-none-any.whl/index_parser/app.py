#!/usr/bin/env python
# coding=utf-8
# Stan 2023-09-23

import os
import json

from flask import Flask

app = Flask(__name__)
# app.config.from_file("config.json", load=json.load)

if not app.secret_key:
    print("SECRET_KEY not set, will use a random key")
    app.secret_key = os.urandom(24)

@app.route('/', defaults={'path': ''}, methods=['OPTIONS'])
@app.route('/<path:path>', methods=['OPTIONS'])
def handle_options(path):
    resp = app.make_default_options_response()
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return resp

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>', methods=['GET'])
def handle_get(path):
    if os.path.isfile('static/%s' % path):
        return app.send_static_file(path)
    else:
        return app.response_class(status=404)

@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def handle_post(path):
    resp = app.response_class(
        response = json.dumps({'path': path}),
        status = 200,
        headers = ( {'Access-Control-Allow-Origin': '*'} ),
        mimetype = 'application/json',
    )
    return resp
