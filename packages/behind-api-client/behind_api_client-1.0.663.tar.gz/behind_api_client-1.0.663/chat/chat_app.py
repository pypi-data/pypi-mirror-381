from .chat_v10 import ChatV10
from .chat_v20 import ChatV20


class ChatApp:
    def __init__(self, api_client):
        self.v10 = ChatV10(api_client)
        self.v20 = ChatV20(api_client)