import can

def get_bus():
    return can.interface.Bus(
        interface='virtual',
        channel='vcan0',
        bitrate=500000
    )