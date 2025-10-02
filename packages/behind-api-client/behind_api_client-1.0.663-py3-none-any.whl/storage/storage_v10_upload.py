class StorageV10Upload:
    def __init__(self, api_client):
        self.api_client = api_client

    def chunk(self):
        """Calls the storage/v10/upload endpoint"""
        return self.api_client.api_request('storage', '10', 'upload', 'chunk', {})

    def remote(self, url):
        """Calls the storage/v10/upload endpoint"""
        return self.api_client.api_request('storage', '10', 'upload', 'remote', {
            "url": url
        })