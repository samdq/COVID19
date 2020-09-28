# app/services.py

from app.models import HospitalBed, Oxygen, Medicine

# Assume data is stored in memory (You would use a database in a real scenario)
hospital_beds_data = []
oxygen_data = []
medicine_data = []

def get_hospital_beds(state, city, pincode):
    # Logic to fetch hospital bed data
    pass