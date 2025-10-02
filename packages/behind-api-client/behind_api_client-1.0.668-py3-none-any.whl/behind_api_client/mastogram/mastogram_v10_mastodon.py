class MastogramV10Mastodon:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the mastogram/v10/mastodon endpoint"""
        return self.api_client.api_request('mastogram', '10', 'mastodon', 'get', {})

    def create(self, domain, token):
        """Calls the mastogram/v10/mastodon endpoint"""
        return self.api_client.api_request('mastogram', '10', 'mastodon', 'create', {
            "domain": domain,
            "token": token
        })

    def update(self, channel_uuid, domain, token, enabled, post, forward, forward_reblogs, forward_bookmarks, privacy, prompt):
        """Calls the mastogram/v10/mastodon endpoint"""
        return self.api_client.api_request('mastogram', '10', 'mastodon', 'update', {
            "channel_uuid": channel_uuid,
            "domain": domain,
            "token": token,
            "enabled": enabled,
            "post": post,
            "forward": forward,
            "forward_reblogs": forward_reblogs,
            "forward_bookmarks": forward_bookmarks,
            "privacy": privacy,
            "prompt": prompt
        })

    def delete(self, channel_uuid):
        """Calls the mastogram/v10/mastodon endpoint"""
        return self.api_client.api_request('mastogram', '10', 'mastodon', 'delete', {
            "channel_uuid": channel_uuid
        })