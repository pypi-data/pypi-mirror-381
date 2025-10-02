from .mastogram_v10 import MastogramV10


class MastogramApp:
    def __init__(self, api_client):
        self.v10 = MastogramV10(api_client)