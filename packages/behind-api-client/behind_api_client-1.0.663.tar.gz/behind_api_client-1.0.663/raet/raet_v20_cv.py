class RaetV20Cv:
    def __init__(self, api_client):
        self.api_client = api_client

    def importFromPdf(self, project_id, file_key):
        """Calls the raet/v20/cv endpoint"""
        return self.api_client.api_request('raet', '20', 'cv', 'importFromPdf', {
            "project_id": project_id,
            "file_key": file_key
        })

    def importFromText(self, project_id, text):
        """Calls the raet/v20/cv endpoint"""
        return self.api_client.api_request('raet', '20', 'cv', 'importFromText', {
            "project_id": project_id,
            "text": text
        })

    def updateFromCallSys(self, cv_id, data):
        """Calls the raet/v20/cv endpoint"""
        return self.api_client.api_request('raet', '20', 'cv', 'updateFromCallSys', {
            "cv_id": cv_id,
            "data": data
        })