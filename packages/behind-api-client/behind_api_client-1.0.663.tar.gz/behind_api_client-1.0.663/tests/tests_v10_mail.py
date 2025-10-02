class TestsV10Mail:
    def __init__(self, api_client):
        self.api_client = api_client

    def getList(self):
        """Calls the tests/v10/mail endpoint"""
        return self.api_client.api_request('tests', '10', 'mail', 'getList', {})