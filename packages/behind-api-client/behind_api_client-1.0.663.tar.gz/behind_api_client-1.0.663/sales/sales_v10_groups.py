class SalesV10Groups:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the sales/v10/groups endpoint"""
        return self.api_client.api_request('sales', '10', 'groups', 'get', {})

    def create(self, name):
        """Calls the sales/v10/groups endpoint"""
        return self.api_client.api_request('sales', '10', 'groups', 'create', {
            "name": name
        })