class MonitorV10Records:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, alias, interval):
        """Calls the monitor/v10/records endpoint"""
        return self.api_client.api_request('monitor', '10', 'records', 'get', {
            "alias": alias,
            "interval": interval
        })

    def financial(self, month):
        """Calls the monitor/v10/records endpoint"""
        return self.api_client.api_request('monitor', '10', 'records', 'financial', {
            "month": month
        })