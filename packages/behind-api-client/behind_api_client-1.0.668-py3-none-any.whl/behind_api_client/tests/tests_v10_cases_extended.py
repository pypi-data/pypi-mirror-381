class TestsV10CasesExtended:
    def __init__(self, api_client):
        self.api_client = api_client

    def testAuthorisation(self):
        """Calls the tests/v10/casesExtended endpoint"""
        return self.api_client.api_request('tests', '10', 'casesExtended', 'testAuthorisation', {})