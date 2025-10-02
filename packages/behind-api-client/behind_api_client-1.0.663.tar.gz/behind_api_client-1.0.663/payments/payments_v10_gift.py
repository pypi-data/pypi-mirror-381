class PaymentsV10Gift:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, code):
        """Calls the payments/v10/gift endpoint"""
        return self.api_client.api_request('payments', '10', 'gift', 'get', {
            "code": code
        })

    def send(self, code, delivery_time, delivery_email, delivery_name, extended):
        """Calls the payments/v10/gift endpoint"""
        return self.api_client.api_request('payments', '10', 'gift', 'send', {
            "code": code,
            "delivery_time": delivery_time,
            "delivery_email": delivery_email,
            "delivery_name": delivery_name,
            "extended": extended
        })

    def apply(self, code):
        """Calls the payments/v10/gift endpoint"""
        return self.api_client.api_request('payments', '10', 'gift', 'apply', {
            "code": code
        })