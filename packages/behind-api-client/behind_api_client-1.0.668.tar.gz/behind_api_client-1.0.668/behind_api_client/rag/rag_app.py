from .rag_v10 import RagV10


class RagApp:
    def __init__(self, api_client):
        self.v10 = RagV10(api_client)