from .raet_v10 import RaetV10
from .raet_v20 import RaetV20


class RaetApp:
    def __init__(self, api_client):
        self.v10 = RaetV10(api_client)
        self.v20 = RaetV20(api_client)