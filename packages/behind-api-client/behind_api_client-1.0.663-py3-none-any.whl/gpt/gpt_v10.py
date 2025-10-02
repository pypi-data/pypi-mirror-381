from .gpt_v10_prompt import GptV10Prompt
from .gpt_v10_storedprompts import GptV10Storedprompts
from .gpt_v10_request import GptV10Request
from .gpt_v10_whisper import GptV10Whisper


class GptV10:
    def __init__(self, api_client):
        self.prompt = GptV10Prompt(api_client)
        self.storedprompts = GptV10Storedprompts(api_client)
        self.request = GptV10Request(api_client)
        self.whisper = GptV10Whisper(api_client)