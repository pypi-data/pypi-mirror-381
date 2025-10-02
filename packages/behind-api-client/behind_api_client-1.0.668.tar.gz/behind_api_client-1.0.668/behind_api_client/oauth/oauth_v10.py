from .oauth_v10_authorisation import OauthV10Authorisation


class OauthV10:
    def __init__(self, api_client):
        self.authorisation = OauthV10Authorisation(api_client)