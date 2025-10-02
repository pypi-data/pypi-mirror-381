class GptV10Prompt:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, custom_prompt, tokens_max, temperature, params):
        """Calls the gpt/v10/prompt endpoint"""
        return self.api_client.api_request('gpt', '10', 'prompt', 'get', {
            "custom_prompt": custom_prompt,
            "tokens_max": tokens_max,
            "temperature": temperature,
            "params": params
        })