from .payments_v10 import PaymentsV10


class PaymentsApp:
    def __init__(self, api_client):
        self.v10 = PaymentsV10(api_client)