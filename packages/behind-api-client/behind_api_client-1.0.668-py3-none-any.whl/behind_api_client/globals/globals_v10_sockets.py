class GlobalsV10Sockets:
    def __init__(self, api_client):
        self.api_client = api_client

    def send(self, user_id, types, message):
        """Calls the globals/v10/sockets endpoint"""
        return self.api_client.api_request('globals', '10', 'sockets', 'send', {
            "user_id": user_id,
            "type": types,
            "message": message
        })