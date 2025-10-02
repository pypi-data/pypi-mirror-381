class OauthV10Authorisation:
    def __init__(self, api_client):
        self.api_client = api_client

    def has(self, user_id, client_id):
        """Calls the oauth/v10/authorisation endpoint"""
        return self.api_client.api_request('oauth', '10', 'authorisation', 'has', {
            "user_id": user_id,
            "client_id": client_id
        })