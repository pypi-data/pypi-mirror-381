class GptV20Prompt:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, prompt_name, params):
        """Calls the gpt/v20/prompt endpoint"""
        return self.api_client.api_request('gpt', '20', 'prompt', 'get', {
            "prompt_name": prompt_name,
            "params": params
        })