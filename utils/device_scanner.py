from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
from utils.logger import setup_logger
import time

logger = setup_logger()


class SmartIPListener(ServiceListener):
    def __init__(self):
        self.devices = []

    def add_service(self, zeroconf, service_type, name):
        try:
            info = zeroconf.get_service_info(service_type, name)
            if info:
                addresses = [
                    "%d.%d.%d.%d" % (addr[0], addr[1], addr[2], addr[3])
                    for addr in info.addresses
                ]
                device_info = f"Service Name: {name}\nIP Address(es): {', '.join(addresses)}\nPort: {info.port}\nProperties: {info.properties}\n"
                self.devices.append(device_info)
                logger.info(f"Found Device: {device_info}")
        except Exception as e:
            logger.error(f"Error processing device {name}: {e}")


def scan_output_devices(service_name="_smart_ip._tcp.local."):
    """Scans for network output devices with a specified service name."""
    try:
        zeroconf = Zeroconf()
        listener = SmartIPListener()
        browser = ServiceBrowser(zeroconf, service_name, listener)

        logger.info(f"Scanning for service: {service_name}...")
        time.sleep(3)  # Allow some time for discovery

        zeroconf.close()
        logger.info("Scanning complete.")
        return listener.devices
    except Exception as e:
        logger.error(f"Error scanning for devices: {e}")
        return []
