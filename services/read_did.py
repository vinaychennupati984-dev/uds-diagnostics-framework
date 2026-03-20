from utils.nrc_decoder import decode_nrc

class ReadDID:
    def __init__(self, uds_client):
        self.client = uds_client

    def read(self, did):
        did_high = (did >> 8) & 0xFF
        did_low = did & 0xFF

        request = [0x22, did_high, did_low]
        response = self.client.send_request(request)

        if response is None:
            raise Exception("No response from ECU")

        if response[0] == 0x62:
            return {
                "status": "positive",
                "did": did,
                "data": response[3:]
            }

        elif response[0] == 0x7F:
            return {
                "status": "negative",
                "error_code": response[2],
                "message": decode_nrc(response[2])
            }

        else:
            raise Exception("Unknown response")