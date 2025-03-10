import sys
from PyQt5.QtWidgets import QApplication
from frontend.ui.main_window import MainWindow
from utils.logger import setup_logger

logger = setup_logger()

if __name__ == "__main__":
    try:
        logger.info("Starting Truehear Application...")
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logger.critical(f"Truehear App Crashed: {e}")
