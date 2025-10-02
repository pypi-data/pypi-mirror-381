from .gpt_v20_prompt import GptV20Prompt


class GptV20:
    def __init__(self, api_client):
        self.prompt = GptV20Prompt(api_client)