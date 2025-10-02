from .gpt_v10 import GptV10
from .gpt_v20 import GptV20
from .gpt_v30 import GptV30
from .gpt_v40 import GptV40


class GptApp:
    def __init__(self, api_client):
        self.v10 = GptV10(api_client)
        self.v20 = GptV20(api_client)
        self.v30 = GptV30(api_client)
        self.v40 = GptV40(api_client)