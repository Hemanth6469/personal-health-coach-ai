import json
import os

DATA_FILE = "data/health_data.json"

def save_health_data(data):

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    with open(DATA_FILE, "r") as f:
        old_data = json.load(f)

    old_data.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(old_data, f, indent=4)
