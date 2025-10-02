class GptV30Prompts:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the gpt/v30/prompts endpoint"""
        return self.api_client.api_request('gpt', '30', 'prompts', 'get', {})

    def create(self, title, temperature, max_tokens, model, body):
        """Calls the gpt/v30/prompts endpoint"""
        return self.api_client.api_request('gpt', '30', 'prompts', 'create', {
            "title": title,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "model": model,
            "body": body
        })

    def init(self):
        """Calls the gpt/v30/prompts endpoint"""
        return self.api_client.api_request('gpt', '30', 'prompts', 'init', {})