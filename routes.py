# app/routes.py

from flask import request, jsonify
from app import app
from app.services import (
    get_hospital_beds,
    get_oxygen,
    get_medicine,
    update_feedback
)

@app.route('/hospital-beds', methods=['GET'])
def hospital_beds():
    state = request.args.get('state')
    city = request.args.get('city')
    pincode = request.args.get('pincode')

    data = get_hospital_beds(state, city, pincode)

    return jsonify(data)

@app.route('/oxygen', methods=['GET'])
def oxygen():
    state = request.args.get('state')
    city = request.args.get('city')
    pincode = request.args.get('pincode')

    data = get_oxygen(state, city, pincode)

    return jsonify(data)

