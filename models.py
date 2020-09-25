# app/models.py

class HospitalBed:
    def __init__(self, state, city, pincode, available_beds):
        self.state = state
        self.city = city
        self.pincode = pincode
        self.available_beds = available_beds