from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QMutexLocker
from collections import deque
from utils.logger import log_queue
import time


class LogUpdaterThread(QThread):
    """Background thread to update logs in UI"""

    new_log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = True  # Flag to control thread execution
        self.log_buffer = deque(maxlen=100)  # Buffer to store logs temporarily
        self.mutex = QMutex()  # Mutex for thread safety

    def run(self):
        while self.running:
            with QMutexLocker(self.mutex):  # Ensure thread safety
                while not log_queue.empty():
                    log_entry = log_queue.get()
                    self.log_buffer.append(log_entry)

            if self.log_buffer:
                self.new_log_signal.emit("\n".join(self.log_buffer))
                self.log_buffer.clear()  # Clear buffer after emitting

            time.sleep(0.2)  # Prevent CPU overuse

    def stop(self):
        """Stops the thread gracefully"""
        self.running = False
        self.wait()


class LogViewer(QWidget):
    """UI Component to display logs in real-time"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Log Display
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)  # Prevent user editing
        self.log_display.setPlaceholderText("Server logs will appear here...")

        # Clear Log Button
        self.clear_button = QPushButton("Clear Logs")
        self.clear_button.clicked.connect(self.clear_logs)

        # Add widgets to layout
        layout.addWidget(self.log_display)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

        # Start log updating thread
        self.log_thread = LogUpdaterThread()
        self.log_thread.new_log_signal.connect(self.append_log)
        self.log_thread.start()

    def append_log(self, log_entry):
        """Appends new log messages to the UI"""
        self.log_display.append(log_entry)
        self.log_display.moveCursor(self.log_display.textCursor().End)  # Auto-scroll

    def clear_logs(self):
        """Clears the log display"""
        self.log_display.clear()

    def closeEvent(self, event):
        """Ensures the log thread stops when UI is closed"""
        self.log_thread.stop()
        event.accept()
