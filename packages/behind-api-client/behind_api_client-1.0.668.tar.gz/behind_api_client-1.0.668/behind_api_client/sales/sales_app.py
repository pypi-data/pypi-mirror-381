from .sales_v10 import SalesV10
from .sales_v20 import SalesV20


class SalesApp:
    def __init__(self, api_client):
        self.v10 = SalesV10(api_client)
        self.v20 = SalesV20(api_client)