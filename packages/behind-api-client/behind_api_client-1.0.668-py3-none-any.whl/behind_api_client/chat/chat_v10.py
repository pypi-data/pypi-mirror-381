from .chat_v10_chat import ChatV10Chat
from .chat_v10_chats import ChatV10Chats
from .chat_v10_message import ChatV10Message


class ChatV10:
    def __init__(self, api_client):
        self.chat = ChatV10Chat(api_client)
        self.chats = ChatV10Chats(api_client)
        self.message = ChatV10Message(api_client)