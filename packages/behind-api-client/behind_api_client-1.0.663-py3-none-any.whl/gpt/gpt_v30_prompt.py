class GptV30Prompt:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, prompt_id):
        """Calls the gpt/v30/prompt endpoint"""
        return self.api_client.api_request('gpt', '30', 'prompt', 'get', {
            "prompt_id": prompt_id
        })

    def execute(self, prompt_id, params):
        """Calls the gpt/v30/prompt endpoint"""
        return self.api_client.api_request('gpt', '30', 'prompt', 'execute', {
            "prompt_id": prompt_id,
            "params": params
        })

    def edit(self, prompt_id, title, temperature, max_tokens, model, body):
        """Calls the gpt/v30/prompt endpoint"""
        return self.api_client.api_request('gpt', '30', 'prompt', 'edit', {
            "prompt_id": prompt_id,
            "title": title,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "model": model,
            "body": body
        })

    def delete(self, prompt_id):
        """Calls the gpt/v30/prompt endpoint"""
        return self.api_client.api_request('gpt', '30', 'prompt', 'delete', {
            "prompt_id": prompt_id
        })