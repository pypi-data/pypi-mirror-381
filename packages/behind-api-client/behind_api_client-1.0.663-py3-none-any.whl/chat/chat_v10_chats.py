class ChatV10Chats:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the chat/v10/chats endpoint"""
        return self.api_client.api_request('chat', '10', 'chats', 'get', {})