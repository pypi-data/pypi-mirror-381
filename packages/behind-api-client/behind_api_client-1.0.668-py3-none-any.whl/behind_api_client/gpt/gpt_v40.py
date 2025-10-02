from .gpt_v40_prompts import GptV40Prompts
from .gpt_v40_prompt import GptV40Prompt


class GptV40:
    def __init__(self, api_client):
        self.prompts = GptV40Prompts(api_client)
        self.prompt = GptV40Prompt(api_client)