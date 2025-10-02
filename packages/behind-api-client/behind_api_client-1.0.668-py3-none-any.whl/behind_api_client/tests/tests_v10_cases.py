class TestsV10Cases:
    def __init__(self, api_client):
        self.api_client = api_client

    def testParameters(self, param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9):
        """Calls the tests/v10/cases endpoint"""
        return self.api_client.api_request('tests', '10', 'cases', 'testParameters', {
            "param_1": param_1,
            "param_2": param_2,
            "param_3": param_3,
            "param_4": param_4,
            "param_5": param_5,
            "param_6": param_6,
            "param_7": param_7,
            "param_8": param_8,
            "param_9": param_9
        })

    def testAuthorisation(self):
        """Calls the tests/v10/cases endpoint"""
        return self.api_client.api_request('tests', '10', 'cases', 'testAuthorisation', {})