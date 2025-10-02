class StorageV10Files:
    def __init__(self, api_client):
        self.api_client = api_client

    def store(self, file_token):
        """Calls the storage/v10/files endpoint"""
        return self.api_client.api_request('storage', '10', 'files', 'store', {
            "file_token": file_token
        })

    def get(self, file_key):
        """Calls the storage/v10/files endpoint"""
        return self.api_client.api_request('storage', '10', 'files', 'get', {
            "file_key": file_key
        })

    def obtain(self, file_key):
        """Calls the storage/v10/files endpoint"""
        return self.api_client.api_request('storage', '10', 'files', 'obtain', {
            "file_key": file_key
        })

    def download(self, object_id):
        """Calls the storage/v10/files endpoint"""
        return self.api_client.api_request('storage', '10', 'files', 'download', {
            "object_id": object_id
        })