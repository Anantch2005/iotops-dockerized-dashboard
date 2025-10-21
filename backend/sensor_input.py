# sensor_input.py
import random

# Later you will replace this with actual ESP32/MQTT/Serial read logic
# Example: read from serial / MQTT / HTTP endpoint
# For now, simulate stable values so backend runs fine

def get_sensor_reading():
    try:
        # 🧠 Example placeholder for ESP32 connection
        # real_temp = read_from_esp32_sensor("temp")
        # real_vib = read_from_esp32_sensor("vibration")
        # return {"temperature": real_temp, "vibration": real_vib}

        # Fallback (temporary simulation)
        return {
            "temperature": round(random.uniform(25, 30), 1),
            "vibration": round(random.uniform(10, 15), 1)
        }
    except Exception as e:
        print("Sensor read failed, using default values:", e)
        return {"temperature": 0, "vibration": 0}
