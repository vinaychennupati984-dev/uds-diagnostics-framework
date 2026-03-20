class SessionControl:
    def __init__(self, uds_client):
        self.client = uds_client

    def change_session(self, session_type):
        response = self.client.send_request([0x10, session_type])

        if response and response[0] == 0x50:
            return {"status": "positive", "session": session_type}

        elif response and response[0] == 0x7F:
            return {"status": "negative", "error_code": response[2]}

        return {"status": "failed"}