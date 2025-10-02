class EasyjobV10Reports:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, application_id):
        """Calls the easyjob/v10/reports endpoint"""
        return self.api_client.api_request('easyjob', '10', 'reports', 'create', {
            "application_id": application_id
        })

    def get(self, application_id):
        """Calls the easyjob/v10/reports endpoint"""
        return self.api_client.api_request('easyjob', '10', 'reports', 'get', {
            "application_id": application_id
        })

    def build(self, application_id):
        """Calls the easyjob/v10/reports endpoint"""
        return self.api_client.api_request('easyjob', '10', 'reports', 'build', {
            "application_id": application_id
        })

    def score(self, application_id):
        """Calls the easyjob/v10/reports endpoint"""
        return self.api_client.api_request('easyjob', '10', 'reports', 'score', {
            "application_id": application_id
        })