from .sales_v10_companies import SalesV10Companies
from .sales_v10_company import SalesV10Company
from .sales_v10_notes import SalesV10Notes
from .sales_v10_group import SalesV10Group
from .sales_v10_groups import SalesV10Groups
from .sales_v10_catalogue import SalesV10Catalogue
from .sales_v10_categories import SalesV10Categories
from .sales_v10_logs import SalesV10Logs


class SalesV10:
    def __init__(self, api_client):
        self.companies = SalesV10Companies(api_client)
        self.company = SalesV10Company(api_client)
        self.notes = SalesV10Notes(api_client)
        self.group = SalesV10Group(api_client)
        self.groups = SalesV10Groups(api_client)
        self.catalogue = SalesV10Catalogue(api_client)
        self.categories = SalesV10Categories(api_client)
        self.logs = SalesV10Logs(api_client)