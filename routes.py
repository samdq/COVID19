# app/routes.py

from flask import request, jsonify
from app import app
from app.services import (
    get_hospital_beds,
    get_oxygen,
    get_medicine,
    update_feedback
)