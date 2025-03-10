import requests
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTextEdit,
)
from PyQt5.QtCore import QThread, pyqtSignal
from utils.logger import log_queue  # Import shared log queue


class ScanThread(QThread):
    """Thread to perform the scan request without freezing the UI"""

    scan_finished = pyqtSignal(object, str)  # Emits (devices_list, error_message)

    def __init__(self, service_name):
        super().__init__()
        self.service_name = service_name

    def run(self):
        """Performs the scan request to the backend"""
        log_queue.put(f"Sending scan request for: {self.service_name}")
        try:
            response = requests.post(
                "http://127.0.0.1:5000/devices/scan",
                json={"service_name": self.service_name},
            )
            if response.status_code == 200:
                devices = response.json().get("devices", [])
                log_queue.put(f"Scan completed. Devices found: {devices}")
                self.scan_finished.emit(devices, None)
            else:
                error_message = response.json().get("error", "Unknown error")
                log_queue.put(f"Scan failed: {error_message}")
                self.scan_finished.emit([], error_message)

        except requests.exceptions.RequestException as e:
            log_queue.put(f"Failed to reach server: {e}")
            self.scan_finished.emit([], f"Failed to reach server: {e}")


class ScanTrigger(QWidget):
    """UI Component to trigger backend scan"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components"""
        layout = QVBoxLayout()

        self.label = QLabel("Enter service name (or leave blank for default):")
        self.service_input = QLineEdit()
        self.service_input.setPlaceholderText("_smart_ip._tcp.local.")

        self.scan_button = QPushButton("Scan Device")
        self.scan_button.clicked.connect(self.scan_devices)

        self.scan_output = QTextEdit()
        self.scan_output.setReadOnly(True)

        layout.addWidget(self.label)
        layout.addWidget(self.service_input)
        layout.addWidget(self.scan_button)
        layout.addWidget(self.scan_output)
        self.setLayout(layout)

    def scan_devices(self):
        """Triggers backend device scan in a separate thread"""
        service_name = self.service_input.text().strip()
        service_name = service_name if service_name else "_smart_ip._tcp.local."

        self.scan_button.setEnabled(False)
        self.scan_output.setText(f"Scanning for {service_name}... Please wait.")
        log_queue.put(f"Initiating scan for {service_name}...")  # Log UI action

        self.scan_thread = ScanThread(service_name)
        self.scan_thread.scan_finished.connect(self.display_scan_results)
        self.scan_thread.start()

    def display_scan_results(self, devices, error_message):
        """Updates UI after scanning is finished"""
        if error_message:
            self.scan_output.append(f"Error: {error_message}")
            log_queue.put(f"Error: {error_message}")
        elif devices:
            self.scan_output.append("Scan complete! Devices found:")
            for device in devices:
                self.scan_output.append(str(device))
                log_queue.put(f"Device found: {device}")
        else:
            self.scan_output.append("No devices found.")
            log_queue.put("No devices found.")

        self.scan_button.setEnabled(True)
