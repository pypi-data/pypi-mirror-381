from .storage_v10 import StorageV10


class StorageApp:
    def __init__(self, api_client):
        self.v10 = StorageV10(api_client)