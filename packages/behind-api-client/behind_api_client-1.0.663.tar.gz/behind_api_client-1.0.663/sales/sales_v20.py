from .sales_v20_companies import SalesV20Companies
from .sales_v20_notes import SalesV20Notes


class SalesV20:
    def __init__(self, api_client):
        self.companies = SalesV20Companies(api_client)
        self.notes = SalesV20Notes(api_client)