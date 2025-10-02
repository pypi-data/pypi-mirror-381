class RaetV10Projects:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the raet/v10/projects endpoint"""
        return self.api_client.api_request('raet', '10', 'projects', 'get', {})