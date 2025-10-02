from .globals_v10 import GlobalsV10


class GlobalsApp:
    def __init__(self, api_client):
        self.v10 = GlobalsV10(api_client)