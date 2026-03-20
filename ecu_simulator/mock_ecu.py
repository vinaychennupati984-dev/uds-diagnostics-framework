def start_mock_ecu(stop_event):
    import can

    bus = can.interface.Bus(interface='virtual', channel='vcan0')

    unlocked = False  # 🔐 Security state
    current_session = 0x01  # default session

    while not stop_event.is_set():
        msg = bus.recv(timeout=1)
        if msg is None:
            continue

        data = list(msg.data)

        # 🔄 Session Control (0x10)
        if data[0] == 0x10:
            current_session = data[1]
            response_data = [0x50, data[1]]

        # 🔐 Security Access (0x27)
        elif data[0] == 0x27:
            if data[1] == 0x01:
                response_data = [0x67, 0x01, 0x12, 0x34]

            elif data[1] == 0x02:
                unlocked = True
                response_data = [0x67, 0x02]

        # ✍️ Write DID (0x2E) – Protected
        elif data[0] == 0x2E:
            if not unlocked:
                response_data = [0x7F, 0x2E, 0x33]  # Security denied
            else:
                response_data = [0x6E, data[1], data[2]]

        # 📖 Read DID (0x22)
        elif data[0] == 0x22:
            if data[1:] == [0xF1, 0x90]:
                response_data = [0x62, 0xF1, 0x90, 0x12, 0x34]
            else:
                response_data = [0x7F, 0x22, 0x31]  # Request Out Of Range

        else:
            continue

        response = can.Message(
            arbitration_id=0x7E8,
            data=response_data,
            is_extended_id=False
        )

        bus.send(response)

    bus.shutdown()