class RaetV10Report:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, project_id, cv_id):
        """Calls the raet/v10/report endpoint"""
        return self.api_client.api_request('raet', '10', 'report', 'get', {
            "project_id": project_id,
            "cv_id": cv_id
        })

    def create(self, project_id, cv_id):
        """Calls the raet/v10/report endpoint"""
        return self.api_client.api_request('raet', '10', 'report', 'create', {
            "project_id": project_id,
            "cv_id": cv_id
        })

    def update(self, project_id, cv_id):
        """Calls the raet/v10/report endpoint"""
        return self.api_client.api_request('raet', '10', 'report', 'update', {
            "project_id": project_id,
            "cv_id": cv_id
        })

    def parseSys(self, cv_id, data):
        """Calls the raet/v10/report endpoint"""
        return self.api_client.api_request('raet', '10', 'report', 'parseSys', {
            "cv_id": cv_id,
            "data": data
        })