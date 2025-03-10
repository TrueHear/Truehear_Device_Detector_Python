from flask import Blueprint, jsonify

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/info", methods=["GET"])
def get_info():
    try:
        sample_data = {
            "id": 1,
            "name": "Sample Data",
            "description": "This is a sample API response",
        }
        return jsonify(sample_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error response
