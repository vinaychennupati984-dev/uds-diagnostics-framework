from services.read_did import ReadDID


def test_read_valid_did(uds_env):
    client = uds_env
    service = ReadDID(client)

    result = service.read(0xF190)

    assert result["status"] == "positive"
    assert result["data"] == [0x12, 0x34]


def test_read_invalid_did(uds_env):
    client = uds_env
    service = ReadDID(client)

    result = service.read(0x1234)

    assert result["status"] == "negative"
    assert result["error_code"] == 0x31  # Request Out Of Range