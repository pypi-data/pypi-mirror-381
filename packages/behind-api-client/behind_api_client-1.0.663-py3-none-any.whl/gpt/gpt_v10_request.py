class GptV10Request:
    def __init__(self, api_client):
        self.api_client = api_client

    def execute(self, path, data, params):
        """Calls the gpt/v10/request endpoint"""
        return self.api_client.api_request('gpt', '10', 'request', 'execute', {
            "path": path,
            "data": data,
            "params": params
        })