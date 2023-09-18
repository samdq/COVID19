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



@app.route('/medicine', methods=['GET'])
def medicine():
    state = request.args.get('state')
    city = request.args.get('city')
    pincode = request.args.get('pincode')

    data = get_medicine(state, city, pincode)

    return jsonify(data)

@app.route('/feedback', methods=['POST'])
def feedback():
    state = request.json.get('state')
    city = request.json.get('city')
    pincode = request.json.get('pincode')
    feedback = request.json.get('feedback')

    update_feedback(state, city, pincode, feedback)

    return jsonify({'message': 'Feedback updated successfully'})