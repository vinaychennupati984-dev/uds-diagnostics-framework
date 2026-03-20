import json

def load_config():
    with open("config/ecu_config.json") as f:
        return json.load(f)