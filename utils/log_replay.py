import can
import time

def replay_log(file_path, bus):
    with open(file_path) as f:
        for line in f:
            parts = line.strip().split()

            arb_id = int(parts[0], 16)
            data = [int(x, 16) for x in parts[1:]]

            msg = can.Message(
                arbitration_id=arb_id,
                data=data,
                is_extended_id=False
            )

            bus.send(msg)
            time.sleep(0.1)