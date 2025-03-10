from flask import Blueprint, jsonify

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/", methods=["GET"])
def home():
    try:
        return jsonify({"message": "Welcome to the Flask + PyQt App!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error response
