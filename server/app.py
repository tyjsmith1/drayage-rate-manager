#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Carrier, Rate

# Views go here!

@app.route('/')
def index():
    return '<h1>Drayage Server</h1>'


#### -------------- User Routes -------------- ####
@app.route('/users')
def users():
    users = User.query.all()
    users_body = [user.to_dict() for user in users]
    res = make_response(
        users_body,
        200
    )
    return res
#### -------------- Rate Routes -------------- ####
@app.route('/rates')
def rates():
    rates = Rate.query.all()
    rates_body = [rate.to_dict() for rate in rates]
    res = make_response(
        rates_body,
        200
    )
    return res
#### -------------- Carrier Routes -------------- ####
@app.route('/carriers')
def carriers():
    carriers = Carrier.query.all()
    carriers_body = [carrier.to_dict() for carrier in carriers]
    res = make_response(
        carriers_body,
        200
    )
    return res

if __name__ == '__main__':
    app.run(port=5555, debug=True)