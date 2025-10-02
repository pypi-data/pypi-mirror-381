from .storage_v10_files import StorageV10Files
from .storage_v10_upload import StorageV10Upload


class StorageV10:
    def __init__(self, api_client):
        self.files = StorageV10Files(api_client)
        self.upload = StorageV10Upload(api_client)