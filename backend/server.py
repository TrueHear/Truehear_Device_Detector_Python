from backend import create_app
from utils.logger import setup_logger, log_queue
import logging
from flask.logging import default_handler

logger = setup_logger()
app = create_app()

# Remove default Flask logger and attach our custom logger
app.logger.removeHandler(default_handler)
app.logger.addHandler(logging.StreamHandler())  
app.logger.addHandler(logger.handlers[0])  # Attach our UI-compatible logger

# Also send Flask logs to log queue
class FlaskQueueLogger(logging.Handler):
    """Custom log handler to send Flask logs to UI"""
    def emit(self, record):
        log_entry = self.format(record)
        log_queue.put(log_entry)  # Push logs to UI queue

flask_queue_logger = FlaskQueueLogger()
flask_queue_logger.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
app.logger.addHandler(flask_queue_logger)  # Attach queue logger to Flask

if __name__ == "__main__":
    try:
        logger.info("Starting Flask Server...")
        app.run(port=5000, debug=False)
    except Exception as e:
        logger.critical(f"Server crashed: {e}")
