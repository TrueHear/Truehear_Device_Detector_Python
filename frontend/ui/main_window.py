from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
from frontend.ui.logger_component import LogViewer
from PyQt5.QtCore import QThread, pyqtSignal
from utils.logger import setup_logger
from utils.device_scanner import scan_output_devices
from frontend.ui.scan_b_component import ScanTrigger

logger = setup_logger()

class ScanThread(QThread):
    """Thread to scan for devices without freezing the UI"""
    scan_finished = pyqtSignal(list)

    def __init__(self, service_name):
        super().__init__()
        self.service_name = service_name

    def run(self):
        devices = scan_output_devices(self.service_name)
        self.scan_finished.emit(devices)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TrueHear Device Lister")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # **Existing UI Components**
        self.label = QLabel("Enter service name (or leave blank for default):")
        self.service_input = QLineEdit()
        self.service_input.setPlaceholderText("_smart_ip._tcp.local.")
        self.device_button = QPushButton("Get Output Devices")
        self.device_output = QTextEdit()
        self.device_output.setReadOnly(True)
        
               # **Scan Device Section (Now a separate component)**
        self.scan_component = ScanTrigger()

        # **Server Logs Section**
        self.server_log_label = QLabel("Server Logs:")
        self.server_log_output = LogViewer()  # Use the new Logger Component

        # **Add widgets to layout**
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.service_input)
        self.layout.addWidget(self.device_button)
        self.layout.addWidget(self.device_output)
        self.layout.addWidget(self.scan_component)  # Scan trigger UI
        self.layout.addWidget(self.server_log_label)  # Add new section
        self.layout.addWidget(self.server_log_output)  # Add log display
        self.setLayout(self.layout)

        # **Connect button to function**
        self.device_button.clicked.connect(self.get_output_devices)

    def get_output_devices(self):
        """Starts scanning for output devices in a separate thread"""
        service_name = self.service_input.text().strip()
        if not service_name:
            service_name = "_smart_ip._tcp.local."

        self.device_output.setText(f"Scanning for {service_name}... Please wait.")
        self.device_button.setEnabled(False)

        self.scan_thread = ScanThread(service_name)
        self.scan_thread.scan_finished.connect(self.display_scan_results)
        self.scan_thread.start()

    def display_scan_results(self, devices):
        """Updates UI after scanning is finished"""
        if devices:
            formatted_devices = "\n".join(devices)
            self.device_output.setText(formatted_devices)
        else:
            self.device_output.setText("N/A")

        self.device_button.setEnabled(True)
