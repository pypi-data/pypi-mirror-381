class ChatV20Chat:
    def __init__(self, api_client):
        self.api_client = api_client

    def getContext(self, chat_uuid):
        """Calls the chat/v20/chat endpoint"""
        return self.api_client.api_request('chat', '20', 'chat', 'getContext', {
            "chat_uuid": chat_uuid
        })