class GlobalsV10Storage:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, key):
        """Calls the globals/v10/storage endpoint"""
        return self.api_client.api_request('globals', '10', 'storage', 'get', {
            "key": key
        })

    def getBulk(self, keys):
        """Calls the globals/v10/storage endpoint"""
        return self.api_client.api_request('globals', '10', 'storage', 'getBulk', {
            "keys": keys
        })

    def sets(self, key, value):
        """Calls the globals/v10/storage endpoint"""
        return self.api_client.api_request('globals', '10', 'storage', 'sets', {
            "key": key,
            "value": value
        })