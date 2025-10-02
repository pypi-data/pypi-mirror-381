class MastogramV10Bluesky:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the mastogram/v10/bluesky endpoint"""
        return self.api_client.api_request('mastogram', '10', 'bluesky', 'get', {})

    def create(self, handle):
        """Calls the mastogram/v10/bluesky endpoint"""
        return self.api_client.api_request('mastogram', '10', 'bluesky', 'create', {
            "handle": handle
        })

    def update(self, channel_uuid, enabled, post, forward, forward_reblogs, forward_bookmarks, privacy, prompt):
        """Calls the mastogram/v10/bluesky endpoint"""
        return self.api_client.api_request('mastogram', '10', 'bluesky', 'update', {
            "channel_uuid": channel_uuid,
            "enabled": enabled,
            "post": post,
            "forward": forward,
            "forward_reblogs": forward_reblogs,
            "forward_bookmarks": forward_bookmarks,
            "privacy": privacy,
            "prompt": prompt
        })

    def delete(self, channel_uuid):
        """Calls the mastogram/v10/bluesky endpoint"""
        return self.api_client.api_request('mastogram', '10', 'bluesky', 'delete', {
            "channel_uuid": channel_uuid
        })