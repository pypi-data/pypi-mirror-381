class SalesV10Categories:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, query, section):
        """Calls the sales/v10/categories endpoint"""
        return self.api_client.api_request('sales', '10', 'categories', 'get', {
            "query": query,
            "section": section
        })