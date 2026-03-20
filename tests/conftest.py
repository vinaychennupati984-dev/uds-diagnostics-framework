import threading
import time
import pytest

from ecu_simulator.mock_ecu import start_mock_ecu
from core.uds_client import UDSClient


@pytest.fixture(scope="module")
def uds_env():
    """
    Sets up mock ECU + UDS client
    Shared across test module
    """
    stop_event = threading.Event()

    ecu_thread = threading.Thread(
        target=start_mock_ecu,
        args=(stop_event,)
    )
    ecu_thread.start()

    time.sleep(1)  # Allow ECU to initialize

    client = UDSClient()

    yield client

    # 🔥 Teardown
    stop_event.set()
    ecu_thread.join()
    client.shutdown()