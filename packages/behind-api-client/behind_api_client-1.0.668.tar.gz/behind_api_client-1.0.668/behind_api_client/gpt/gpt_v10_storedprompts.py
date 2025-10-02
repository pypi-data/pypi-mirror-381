class GptV10Storedprompts:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the gpt/v10/storedprompts endpoint"""
        return self.api_client.api_request('gpt', '10', 'storedprompts', 'get', {})