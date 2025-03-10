from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QWidget

class DeviceScannerUI(QWidget):
    """UI Component for scanning devices"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Label
        self.label = QLabel("Enter service name (or leave blank for default):")

        # Service Name Input
        self.service_input = QLineEdit()
        self.service_input.setPlaceholderText("_smart_ip._tcp.local.")

        # Button for Getting Output Devices
        self.device_button = QPushButton("Get Output Devices")
        self.device_output = QTextEdit()
        self.device_output.setReadOnly(True)

        # Add widgets to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.service_input)
        self.layout.addWidget(self.device_button)
        self.layout.addWidget(self.device_output)

        self.setLayout(self.layout)
