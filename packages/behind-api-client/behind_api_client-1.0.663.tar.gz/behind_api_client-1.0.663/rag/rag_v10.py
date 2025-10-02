from .rag_v10_storage import RagV10Storage


class RagV10:
    def __init__(self, api_client):
        self.storage = RagV10Storage(api_client)