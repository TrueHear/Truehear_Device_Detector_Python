# frontend/main.py (Corrected Version)
from frontend.ui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from utils.logger import setup_logger

logger = setup_logger()

def create_main_window():
    """Function to create and return the main window."""
    window = MainWindow()
    return window
