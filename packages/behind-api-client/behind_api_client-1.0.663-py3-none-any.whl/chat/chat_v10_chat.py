class ChatV10Chat:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, chat_uuid):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'get', {
            "chat_uuid": chat_uuid
        })

    def getIdByMember(self, member_id):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'getIdByMember', {
            "member_id": member_id
        })

    def info(self, chat_uuid):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'info', {
            "chat_uuid": chat_uuid
        })

    def pin(self, chat_uuid):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'pin', {
            "chat_uuid": chat_uuid
        })

    def unPin(self, chat_uuid):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'unPin', {
            "chat_uuid": chat_uuid
        })

    def delete(self, chat_uuid):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'delete', {
            "chat_uuid": chat_uuid
        })

    def rename(self, chat_uuid, title):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'rename', {
            "chat_uuid": chat_uuid,
            "title": title
        })

    def create(self, name, member_id, member_name, member_alias, company_id, individual_id):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'create', {
            "name": name,
            "member_id": member_id,
            "member_name": member_name,
            "member_alias": member_alias,
            "company_id": company_id,
            "individual_id": individual_id
        })

    def systemCreate(self, user_id, name, member_id, member_name, individual_id):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'systemCreate', {
            "user_id": user_id,
            "name": name,
            "member_id": member_id,
            "member_name": member_name,
            "individual_id": individual_id
        })

    def systemGetIdByMember(self, member_id):
        """Calls the chat/v10/chat endpoint"""
        return self.api_client.api_request('chat', '10', 'chat', 'systemGetIdByMember', {
            "member_id": member_id
        })