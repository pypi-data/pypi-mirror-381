class RaetV10Project:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, project_id):
        """Calls the raet/v10/project endpoint"""
        return self.api_client.api_request('raet', '10', 'project', 'get', {
            "project_id": project_id
        })

    def create(self):
        """Calls the raet/v10/project endpoint"""
        return self.api_client.api_request('raet', '10', 'project', 'create', {})

    def edit(self, project_id, name, description):
        """Calls the raet/v10/project endpoint"""
        return self.api_client.api_request('raet', '10', 'project', 'edit', {
            "project_id": project_id,
            "name": name,
            "description": description
        })

    def editSys(self, project_id, name, description):
        """Calls the raet/v10/project endpoint"""
        return self.api_client.api_request('raet', '10', 'project', 'editSys', {
            "project_id": project_id,
            "name": name,
            "description": description
        })

    def delete(self, project_id):
        """Calls the raet/v10/project endpoint"""
        return self.api_client.api_request('raet', '10', 'project', 'delete', {
            "project_id": project_id
        })

    def updateStatusSys(self, project_id, status):
        """Calls the raet/v10/project endpoint"""
        return self.api_client.api_request('raet', '10', 'project', 'updateStatusSys', {
            "project_id": project_id,
            "status": status
        })

    def getCallLog(self, project_id):
        """Calls the raet/v10/project endpoint"""
        return self.api_client.api_request('raet', '10', 'project', 'getCallLog', {
            "project_id": project_id
        })