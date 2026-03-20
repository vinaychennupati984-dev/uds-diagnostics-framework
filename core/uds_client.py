from utils.config_loader import load_config
from utils.logger import setup_logger
from core.can_interface import get_bus
import can

class UDSClient:
    def __init__(self):
        self.bus = get_bus()
        config = load_config()

        self.tx_id = config["tx_id"]
        self.rx_id = config["rx_id"]

        self.logger = setup_logger()

    def send_request(self, data, retries=3):
        for attempt in range(retries):
            try:
                msg = can.Message(
                    arbitration_id=self.tx_id,
                    data=data,
                    is_extended_id=False
                )

                self.logger.info(f"Attempt {attempt+1}: Sending {data}")
                self.bus.send(msg)

                response = self.bus.recv(timeout=2)

                if response:
                    res_data = list(response.data)
                    self.logger.info(f"Received: {res_data}")
                    return res_data

            except Exception as e:
                self.logger.error(f"Error: {e}")

            self.logger.warning("Retrying...")

        self.logger.error("Request failed after retries")
        return None

    def shutdown(self):
        if self.bus:
            self.bus.shutdown()