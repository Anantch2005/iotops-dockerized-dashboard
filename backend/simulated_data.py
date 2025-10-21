import random

def generate_fake_reading():
    return {
        "temperature": round(random.uniform(20, 50), 1),
        "vibration": round(random.uniform(5, 40), 1)
    }
