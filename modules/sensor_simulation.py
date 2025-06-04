# sensor_simulation.py
import random
import time
import csv

def generate_sensor_data():
    return {
        "timestamp": time.time(),
        "flow_rate": round(random.uniform(20, 50), 2),
        "turbidity": round(random.uniform(0.5, 5.0), 2),
        "ph": round(random.uniform(6.5, 8.5), 2)
    }

def run_sensor_simulation(filepath, interval=2):
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "flow_rate", "turbidity", "ph"])
        writer.writeheader()

        while True:
            reading = generate_sensor_data()
            writer.writerow(reading)
            print(reading)
            time.sleep(interval)

with open("../data/readings.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["timestamp", "flow_rate", "turbidity", "ph"])
    writer.writeheader()

    while True:
        reading = generate_sensor_data()
        writer.writerow(reading)
        print(reading)
        time.sleep(2)