from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Smart Shoe API Running"

@app.route('/weight', methods=['GET'])
def get_weight():
    """Returns simulated weight data"""
    weight = round(random.uniform(50, 90), 2)  # Simulating weight in kg
    return jsonify({"weight": weight})

@app.route('/location', methods=['GET'])
def get_location():
    """Returns a fake GPS location"""
    lat, lon = 12.9716, 77.5946  # Simulated location (Bangalore)
    return jsonify({"location": f"Lat: {lat}, Lng: {lon}"})

@app.route('/alert', methods=['POST'])
def send_alert():
    """Simulates sending an emergency SMS alert"""
    return jsonify({"status": "Emergency Alert Sent Successfully!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
