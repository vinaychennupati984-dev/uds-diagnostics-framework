import argparse
import threading
import time

from core.uds_client import UDSClient
from services.read_did import ReadDID
from services.write_did import WriteDID
from services.session_control import SessionControl
from services.security_access import SecurityAccess
from ecu_simulator.mock_ecu import start_mock_ecu


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--service", required=True)
    parser.add_argument("--did", type=lambda x: int(x, 16), default=None)
    parser.add_argument("--data", nargs="+", type=lambda x: int(x, 16))

    args = parser.parse_args()

    # 🔥 Start Mock ECU
    stop_event = threading.Event()
    ecu_thread = threading.Thread(target=start_mock_ecu, args=(stop_event,))
    ecu_thread.start()

    time.sleep(1)  # allow ECU to initialize

    client = UDSClient()

    try:
        # 📖 READ DID
        if args.service == "read_did":
            service = ReadDID(client)
            result = service.read(args.did)

        # 🔐 + ✍️ WRITE DID (with security)
        elif args.service == "write_did":
            if not args.data:
                print(" Please provide --data for write_did (e.g. --data 0xAA 0xBB)")
                return

            # Step 1: Security Access
            sec = SecurityAccess(client)

            seed = sec.request_seed()
            print(f"Seed received: {seed}")

            key = [0x00, 0x00]  # dummy key (mock ECU accepts anything)
            if not sec.send_key(key):
                print(" Security Unlock Failed")
                return

            print(" Security Unlocked")

            # Step 2: Write DID
            service = WriteDID(client)
            result = service.write(args.did, args.data)

        # 🔄 SESSION CONTROL
        elif args.service == "session":
            service = SessionControl(client)
            result = service.change_session(0x03)

        else:
            print("Unknown service")
            return

        print("📦 Result:", result)

    finally:
        # 🔥 Clean shutdown
        stop_event.set()
        ecu_thread.join()
        client.shutdown()


if __name__ == "__main__":
    main()