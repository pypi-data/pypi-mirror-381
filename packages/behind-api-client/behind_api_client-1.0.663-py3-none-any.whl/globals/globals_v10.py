from .globals_v10_storage import GlobalsV10Storage
from .globals_v10_sockets import GlobalsV10Sockets


class GlobalsV10:
    def __init__(self, api_client):
        self.storage = GlobalsV10Storage(api_client)
        self.sockets = GlobalsV10Sockets(api_client)