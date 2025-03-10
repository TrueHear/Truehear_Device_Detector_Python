from flask import Flask, jsonify
from backend.routes import api_blueprint
from utils.logger import setup_logger

logger = setup_logger()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)

    # Global Error Handling
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Internal Server Error: {error}")
        return jsonify({"error": "Internal Server Error"}), 500

    @app.errorhandler(404)
    def not_found(error):
        logger.warning("API Route Not Found")
        return jsonify({"error": "Not Found"}), 404

    return app
