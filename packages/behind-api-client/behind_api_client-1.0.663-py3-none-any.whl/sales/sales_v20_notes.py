class SalesV20Notes:
    def __init__(self, api_client):
        self.api_client = api_client

    def add(self, company_id, text, types, data):
        """Calls the sales/v20/notes endpoint"""
        return self.api_client.api_request('sales', '20', 'notes', 'add', {
            "company_id": company_id,
            "text": text,
            "type": types,
            "data": data
        })