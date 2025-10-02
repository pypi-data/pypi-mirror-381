from .tests_v10_core import TestsV10Core
from .tests_v10_cases import TestsV10Cases
from .tests_v10_cases_extended import TestsV10CasesExtended
from .tests_v10_mail import TestsV10Mail


class TestsV10:
    def __init__(self, api_client):
        self.core = TestsV10Core(api_client)
        self.cases = TestsV10Cases(api_client)
        self.cases_extended = TestsV10CasesExtended(api_client)
        self.mail = TestsV10Mail(api_client)