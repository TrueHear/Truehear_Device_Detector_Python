from flask import Blueprint, request, jsonify
from utils.device_scanner import scan_output_devices
import json
import os

devices_blueprint = Blueprint("devices", __name__)

DATA_FILE = "backend/data/database.json"


def save_to_database(data):
    """Saves scanned devices to a JSON file"""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        existing_data["devices"] = data  # Store scanned devices

        with open(DATA_FILE, "w") as file:
            json.dump(existing_data, file, indent=4)

    except Exception as e:
        print(f"Error saving to database: {e}")


@devices_blueprint.route("/scan", methods=["POST"])
def scan_devices():
    """Scans for devices using the given service name"""
    try:
        service_name = request.json.get("service_name", "_smart_ip._tcp.local.")
        devices = scan_output_devices(service_name)
        print("[+] Devices:", devices)
        save_to_database(devices)  # Store found devices in JSON file

        return jsonify({"message": "Scan complete", "devices": devices}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
