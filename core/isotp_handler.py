import isotp
from core.can_interface import get_bus

def get_isotp_stack(tx_id, rx_id):
    bus = get_bus()

    address = isotp.Address(
        isotp.AddressingMode.Normal_11bits,
        txid=tx_id,
        rxid=rx_id
    )

    stack = isotp.CanStack(
        bus=bus,
        address=address
    )

    return stack