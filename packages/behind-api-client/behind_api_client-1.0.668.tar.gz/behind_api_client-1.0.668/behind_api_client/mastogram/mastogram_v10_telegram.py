class MastogramV10Telegram:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the mastogram/v10/telegram endpoint"""
        return self.api_client.api_request('mastogram', '10', 'telegram', 'get', {})

    def create(self):
        """Calls the mastogram/v10/telegram endpoint"""
        return self.api_client.api_request('mastogram', '10', 'telegram', 'create', {})

    def update(self, channel_uuid, enabled, post, forward, prompt):
        """Calls the mastogram/v10/telegram endpoint"""
        return self.api_client.api_request('mastogram', '10', 'telegram', 'update', {
            "channel_uuid": channel_uuid,
            "enabled": enabled,
            "post": post,
            "forward": forward,
            "prompt": prompt
        })

    def delete(self, channel_uuid):
        """Calls the mastogram/v10/telegram endpoint"""
        return self.api_client.api_request('mastogram', '10', 'telegram', 'delete', {
            "channel_uuid": channel_uuid
        })