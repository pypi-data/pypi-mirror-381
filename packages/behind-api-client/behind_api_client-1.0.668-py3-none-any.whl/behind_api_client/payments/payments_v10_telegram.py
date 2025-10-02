class PaymentsV10Telegram:
    def __init__(self, api_client):
        self.api_client = api_client

    def billCreate(self, subscription_id):
        """Calls the payments/v10/telegram endpoint"""
        return self.api_client.api_request('payments', '10', 'telegram', 'billCreate', {
            "subscription_id": subscription_id
        })

    def billCreateUnauthorised(self, subscription_id, user_id, redirect_url):
        """Calls the payments/v10/telegram endpoint"""
        return self.api_client.api_request('payments', '10', 'telegram', 'billCreateUnauthorised', {
            "subscription_id": subscription_id,
            "user_id": user_id,
            "redirect_url": redirect_url
        })

    def billStatus(self, bill_id):
        """Calls the payments/v10/telegram endpoint"""
        return self.api_client.api_request('payments', '10', 'telegram', 'billStatus', {
            "bill_id": bill_id
        })

    def start(self, ctx):
        """Calls the payments/v10/telegram endpoint"""
        return self.api_client.api_request('payments', '10', 'telegram', 'start', {
            "ctx": ctx
        })

    def successfulPayment(self, ctx):
        """Calls the payments/v10/telegram endpoint"""
        return self.api_client.api_request('payments', '10', 'telegram', 'successfulPayment', {
            "ctx": ctx
        })