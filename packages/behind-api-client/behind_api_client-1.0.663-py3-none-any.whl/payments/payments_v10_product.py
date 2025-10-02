class PaymentsV10Product:
    def __init__(self, api_client):
        self.api_client = api_client

    def has(self, user_id, product_id):
        """Calls the payments/v10/product endpoint"""
        return self.api_client.api_request('payments', '10', 'product', 'has', {
            "user_id": user_id,
            "product_id": product_id
        })