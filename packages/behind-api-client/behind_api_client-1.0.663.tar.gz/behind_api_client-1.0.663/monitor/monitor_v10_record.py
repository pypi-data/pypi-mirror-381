class MonitorV10Record:
    def __init__(self, api_client):
        self.api_client = api_client

    def add(self, alias, value):
        """Calls the monitor/v10/record endpoint"""
        return self.api_client.api_request('monitor', '10', 'record', 'add', {
            "alias": alias,
            "value": value
        })