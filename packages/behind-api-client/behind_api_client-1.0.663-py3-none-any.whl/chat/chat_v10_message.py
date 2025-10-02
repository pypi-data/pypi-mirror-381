class ChatV10Message:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, chat_uuid, text, types):
        """Calls the chat/v10/message endpoint"""
        return self.api_client.api_request('chat', '10', 'message', 'create', {
            "chat_uuid": chat_uuid,
            "text": text,
            "type": types
        })

    def createFrom(self, chat_uuid, froms, text):
        """Calls the chat/v10/message endpoint"""
        return self.api_client.api_request('chat', '10', 'message', 'createFrom', {
            "chat_uuid": chat_uuid,
            "from": froms,
            "text": text
        })

    def setStatus(self, msg_uuid, status):
        """Calls the chat/v10/message endpoint"""
        return self.api_client.api_request('chat', '10', 'message', 'setStatus', {
            "msg_uuid": msg_uuid,
            "status": status
        })

    def edit(self, msg_uuid, text):
        """Calls the chat/v10/message endpoint"""
        return self.api_client.api_request('chat', '10', 'message', 'edit', {
            "msg_uuid": msg_uuid,
            "text": text
        })

    def delete(self, msg_uuid):
        """Calls the chat/v10/message endpoint"""
        return self.api_client.api_request('chat', '10', 'message', 'delete', {
            "msg_uuid": msg_uuid
        })

    def render(self, chat_uuid, prompt, extended):
        """Calls the chat/v10/message endpoint"""
        return self.api_client.api_request('chat', '10', 'message', 'render', {
            "chat_uuid": chat_uuid,
            "prompt": prompt,
            "extended": extended
        })