NRC_CODES = {
    0x10: "General Reject",
    0x11: "Service Not Supported",
    0x12: "SubFunction Not Supported",
    0x31: "Request Out Of Range",
    0x33: "Security Access Denied"
}

def decode_nrc(code):
    return NRC_CODES.get(code, "Unknown NRC")