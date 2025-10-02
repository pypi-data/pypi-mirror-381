class TestsV10Core:
    def __init__(self, api_client):
        self.api_client = api_client

    def reAssignToken(self, access_token):
        """Calls the tests/v10/core endpoint"""
        return self.api_client.api_request('tests', '10', 'core', 'reAssignToken', {
            "access_token": access_token
        })