from .tests_v10 import TestsV10


class TestsApp:
    def __init__(self, api_client):
        self.v10 = TestsV10(api_client)