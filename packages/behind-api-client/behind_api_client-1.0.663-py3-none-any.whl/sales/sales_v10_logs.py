class SalesV10Logs:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the sales/v10/logs endpoint"""
        return self.api_client.api_request('sales', '10', 'logs', 'get', {})