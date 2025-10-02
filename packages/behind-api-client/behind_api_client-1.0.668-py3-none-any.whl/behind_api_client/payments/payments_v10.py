from .payments_v10_payture import PaymentsV10Payture
from .payments_v10_telegram import PaymentsV10Telegram
from .payments_v10_product import PaymentsV10Product
from .payments_v10_gift import PaymentsV10Gift


class PaymentsV10:
    def __init__(self, api_client):
        self.payture = PaymentsV10Payture(api_client)
        self.telegram = PaymentsV10Telegram(api_client)
        self.product = PaymentsV10Product(api_client)
        self.gift = PaymentsV10Gift(api_client)