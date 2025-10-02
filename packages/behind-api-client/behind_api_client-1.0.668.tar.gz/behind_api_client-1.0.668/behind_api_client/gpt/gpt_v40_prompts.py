class GptV40Prompts:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the gpt/v40/prompts endpoint"""
        return self.api_client.api_request('gpt', '40', 'prompts', 'get', {})

    def create(self, title, body, extended):
        """Calls the gpt/v40/prompts endpoint"""
        return self.api_client.api_request('gpt', '40', 'prompts', 'create', {
            "title": title,
            "body": body,
            "extended": extended
        })

    def init(self):
        """Calls the gpt/v40/prompts endpoint"""
        return self.api_client.api_request('gpt', '40', 'prompts', 'init', {})