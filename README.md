# COVID-19 Tracker

This repository contains a REST API package that consolidates and provides real-time data on the availability of hospital beds, oxygen, and medicines across multiple sources for COVID-19. The data is updated every 30 minutes and is segmented by state, city, and pincode.

## API Endpoints

### Hospital Beds

- Endpoint: /hospital-beds
- Method: GET
- Parameters:
- state (required): State name
- city (required): City name
- pincode (required): Pincode
- Example: http://localhost:5000/hospital-beds?state=STATE&city=CITY&pincode=PINCODE

### Oxygen

- Endpoint: /oxygen
- Method: GET
- Parameters:
- state (required): State name
- city (required): City name
- pincode (required): Pincode
- Example: http://localhost:5000/oxygen?state=STATE&city=CITY&pincode=PINCODE


### Medicine

- Endpoint: /medicine
- Method: GET
- Parameters:
- state (required): State name
- city (required): City name
- pincode (required): Pincode
- Example: http://localhost:5000/medicine?state=STATE&city=CITY&pincode=PINCODE

## Getting Started

### Clone the repository:

- git clone https://github.com/your-username/covid-tracker.git
- Navigate to the project directory:



- Install the required packages:

```
pip install -r requirements.txt
```

- Run the application:

```
python run.py
```

- Access the APIs using the provided endpoints.


## Dependencies

- Flask 2.0.1

## Note

- This application uses in-memory data storage for demonstration purposes. In a production environment, you should replace it with a proper database.
- Ensure proper error handling, authentication, and security measures in a production environment.

Remember to replace the placeholders like STATE, CITY, PINCODE, and your-username with actual values. This README provides a basic structure, and you can customize it based on your project's specifics.


## Directory Structure:

covid_tracker/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── services.py
├── config.py
├── requirements.txt
└── run.py


