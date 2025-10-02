class RagV10Storage:
    def __init__(self, api_client):
        self.api_client = api_client

    def search(self, query, limit):
        """Calls the rag/v10/storage endpoint"""
        return self.api_client.api_request('rag', '10', 'storage', 'search', {
            "query": query,
            "limit": limit
        })

    def put(self, text, doc_type, source, book_id, chapter_id, page_id):
        """Calls the rag/v10/storage endpoint"""
        return self.api_client.api_request('rag', '10', 'storage', 'put', {
            "text": text,
            "doc_type": doc_type,
            "source": source,
            "book_id": book_id,
            "chapter_id": chapter_id,
            "page_id": page_id
        })