import sys
from frontend.main import MainWindow, QApplication
import atexit
from multiprocessing import Process
from backend.server import app
from PyQt5.QtWidgets import QApplication
from utils.logger import setup_logger

logger = setup_logger()
server_process = None  # Global reference to the server process


def run_server():
    """Runs Flask server in a separate process"""
    try:
        logger.info("Starting Flask Server Process...")
        app.run(port=5000, debug=False)
    except Exception as e:
        logger.critical(f"Flask Server Crashed: {e}")


def stop_server():
    """Stops the Flask server process if running"""
    global server_process
    if server_process and server_process.is_alive():
        logger.info("Stopping Flask Server...")
        server_process.terminate()  # Terminate the server process
        server_process.join()
        logger.info("Flask Server Stopped.")


if __name__ == "__main__":
    try:
        # Start Flask Server in a separate process
        server_process = Process(target=run_server)
        server_process.start()

        # Ensure the server stops when the application exits
        atexit.register(stop_server)

        # Start PyQt Application
        logger.info("Launching PyQt UI...")
        app = QApplication(sys.argv)
        window = MainWindow()

        # When user closes the window, stop the server
        window.destroyed.connect(stop_server)

        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logger.critical(f"Application Crashed: {e}")
        stop_server()  # Ensure server is stopped even if there's an error
