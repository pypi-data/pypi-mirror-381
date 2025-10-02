class MonitorV10Finances:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, month):
        """Calls the monitor/v10/finances endpoint"""
        return self.api_client.api_request('monitor', '10', 'finances', 'get', {
            "month": month
        })

    def sets(self, alias, month, value):
        """Calls the monitor/v10/finances endpoint"""
        return self.api_client.api_request('monitor', '10', 'finances', 'sets', {
            "alias": alias,
            "month": month,
            "value": value
        })

    def accountGet(self, month):
        """Calls the monitor/v10/finances endpoint"""
        return self.api_client.api_request('monitor', '10', 'finances', 'accountGet', {
            "month": month
        })

    def accountSet(self, alias, month, value):
        """Calls the monitor/v10/finances endpoint"""
        return self.api_client.api_request('monitor', '10', 'finances', 'accountSet', {
            "alias": alias,
            "month": month,
            "value": value
        })