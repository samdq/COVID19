# app/models.py


class Oxygen:
    def __init__(self, state, city, pincode, available_oxygen):
        self.state = state
        self.city = city
        self.pincode = pincode
        self.available_oxygen = available_oxygen
        
class Medicine:
    def __init__(self, state, city, pincode, available_medicines):
        self.state = state
        self.city = city
        self.pincode = pincode
        self.available_medicines = available_medicines