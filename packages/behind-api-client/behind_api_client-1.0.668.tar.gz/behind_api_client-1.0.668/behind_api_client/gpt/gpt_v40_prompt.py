class GptV40Prompt:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, prompt_id):
        """Calls the gpt/v40/prompt endpoint"""
        return self.api_client.api_request('gpt', '40', 'prompt', 'get', {
            "prompt_id": prompt_id
        })

    def edit(self, prompt_id, title, extended, body):
        """Calls the gpt/v40/prompt endpoint"""
        return self.api_client.api_request('gpt', '40', 'prompt', 'edit', {
            "prompt_id": prompt_id,
            "title": title,
            "extended": extended,
            "body": body
        })