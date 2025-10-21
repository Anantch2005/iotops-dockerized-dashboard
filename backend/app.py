from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
import time
import os

from simulated_data import generate_fake_reading
from sensor_input import get_sensor_reading

app = Flask(__name__)
CORS(app)

# Environment flag: USE_SIMULATED=true/false
USE_SIMULATED = os.environ.get("USE_SIMULATED", "true").lower() == "true"

# Store thresholds and recent data
thresholds = {"temp": 35, "vib": 25}
sensor_data = []

def update_data():
    global sensor_data
    while True:
        if USE_SIMULATED:
            reading = generate_fake_reading()
        else:
            reading = get_sensor_reading()
        sensor_data.append(reading)
        if len(sensor_data) > 30:
            sensor_data.pop(0)
        time.sleep(3)

# Start background thread
threading.Thread(target=update_data, daemon=True).start()

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(sensor_data)

@app.route("/api/threshold", methods=["POST"])
def update_threshold():
    global thresholds
    data = request.json
    ttype = data.get("type")
    value = data.get("value")
    if ttype in thresholds:
        thresholds[ttype] = value
    return jsonify({"status": "updated", "thresholds": thresholds})

@app.route("/api/mode", methods=["GET"])
def mode():
    mode = "Simulated" if USE_SIMULATED else "Sensor"
    return jsonify({"mode": mode})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
