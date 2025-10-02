from .gpt_v30_prompt import GptV30Prompt
from .gpt_v30_prompts import GptV30Prompts
from .gpt_v30_chat import GptV30Chat


class GptV30:
    def __init__(self, api_client):
        self.prompt = GptV30Prompt(api_client)
        self.prompts = GptV30Prompts(api_client)
        self.chat = GptV30Chat(api_client)