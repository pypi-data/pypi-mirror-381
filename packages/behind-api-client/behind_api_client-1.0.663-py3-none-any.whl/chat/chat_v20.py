from .chat_v20_chat import ChatV20Chat
from .chat_v20_message import ChatV20Message


class ChatV20:
    def __init__(self, api_client):
        self.chat = ChatV20Chat(api_client)
        self.message = ChatV20Message(api_client)