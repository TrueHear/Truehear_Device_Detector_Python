import logging
import sys
from multiprocessing import Queue

log_queue = Queue()  # Shared queue for UI logs


class QueueLogger(logging.Handler):
    """Custom log handler to send logs to the UI through a queue"""

    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        log_entry = self.format(record)
        self.log_queue.put(log_entry)  # Send logs to the queue


def setup_logger():
    """Configures logging system for both console and UI queue"""
    logger = logging.getLogger("TrueHearLogger")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    queue_handler = QueueLogger(log_queue)
    queue_handler.setLevel(logging.DEBUG)
    queue_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    logger.addHandler(console_handler)
    logger.addHandler(queue_handler)

    return logger
