from .oauth_v10 import OauthV10


class OauthApp:
    def __init__(self, api_client):
        self.v10 = OauthV10(api_client)