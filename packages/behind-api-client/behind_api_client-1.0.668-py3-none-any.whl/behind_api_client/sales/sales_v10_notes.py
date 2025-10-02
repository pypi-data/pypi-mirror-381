class SalesV10Notes:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, page, page_size):
        """Calls the sales/v10/notes endpoint"""
        return self.api_client.api_request('sales', '10', 'notes', 'get', {
            "page": page,
            "page_size": page_size
        })

    def add(self, company_id, text):
        """Calls the sales/v10/notes endpoint"""
        return self.api_client.api_request('sales', '10', 'notes', 'add', {
            "company_id": company_id,
            "text": text
        })

    def edit(self, note_id, text):
        """Calls the sales/v10/notes endpoint"""
        return self.api_client.api_request('sales', '10', 'notes', 'edit', {
            "note_id": note_id,
            "text": text
        })

    def delete(self, note_id):
        """Calls the sales/v10/notes endpoint"""
        return self.api_client.api_request('sales', '10', 'notes', 'delete', {
            "note_id": note_id
        })