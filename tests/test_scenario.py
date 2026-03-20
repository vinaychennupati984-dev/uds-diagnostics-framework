from services.read_did import ReadDID
from services.write_did import WriteDID
from services.security_access import SecurityAccess
from services.session_control import SessionControl


def test_full_diagnostic_flow(uds_env):
    client = uds_env

    # 🔄 Step 1: Session Control
    session = SessionControl(client)
    session_result = session.change_session(0x03)
    assert session_result["status"] == "positive"

    # 🔐 Step 2: Security Access
    sec = SecurityAccess(client)

    seed = sec.request_seed()
    assert seed is not None

    key = [0x00, 0x00]  # dummy key
    unlock = sec.send_key(key)
    assert unlock is True

    # ✍️ Step 3: Write DID
    write = WriteDID(client)
    write_result = write.write(0xF190, [0xAA, 0xBB])
    assert write_result["status"] == "positive"

    # 📖 Step 4: Read DID
    read = ReadDID(client)
    read_result = read.read(0xF190)

    assert read_result["status"] == "positive"