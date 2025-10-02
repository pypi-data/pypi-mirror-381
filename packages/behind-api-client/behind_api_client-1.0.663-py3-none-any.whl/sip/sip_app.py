from .sip_v10 import SipV10


class SipApp:
    def __init__(self, api_client):
        self.v10 = SipV10(api_client)