class SecurityAccess:
    def __init__(self, uds_client):
        self.client = uds_client

    def request_seed(self):
        response = self.client.send_request([0x27, 0x01])

        if response and response[0] == 0x67:
            return response[2:]

        raise Exception("Seed request failed")

    def send_key(self, key):
        response = self.client.send_request([0x27, 0x02] + key)

        if response and response[0] == 0x67:
            return True

        return False