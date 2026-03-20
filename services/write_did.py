class WriteDID:
    def __init__(self, uds_client):
        self.client = uds_client

    def write(self, did, data):
        did_high = (did >> 8) & 0xFF
        did_low = did & 0xFF

        request = [0x2E, did_high, did_low] + data
        response = self.client.send_request(request)

        if response and response[0] == 0x6E:
            return {"status": "positive"}

        elif response and response[0] == 0x7F:
            return {"status": "negative", "error_code": response[2]}

        return {"status": "failed"}