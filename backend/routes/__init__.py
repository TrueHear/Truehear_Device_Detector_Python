from flask import Blueprint
from backend.routes.home import home_blueprint
from backend.routes.data import data_blueprint
from backend.routes.devices_routes import devices_blueprint
# Main Blueprint to register all routes
api_blueprint = Blueprint("api", __name__)

# Register individual blueprints
api_blueprint.register_blueprint(home_blueprint, url_prefix="/home")
api_blueprint.register_blueprint(data_blueprint, url_prefix="/data")
api_blueprint.register_blueprint(devices_blueprint, url_prefix="/devices")
