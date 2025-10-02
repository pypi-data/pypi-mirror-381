from .easyjob_v10 import EasyjobV10


class EasyjobApp:
    def __init__(self, api_client):
        self.v10 = EasyjobV10(api_client)