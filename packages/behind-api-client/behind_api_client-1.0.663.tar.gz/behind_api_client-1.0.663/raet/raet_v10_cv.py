class RaetV10Cv:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, individual_id):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'get', {
            "individual_id": individual_id
        })

    def create(self, individual_id, cv):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'create', {
            "individual_id": individual_id,
            "cv": cv
        })

    def update(self, cv_id, cv):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'update', {
            "cv_id": cv_id,
            "cv": cv
        })

    def updateOutline(self, cv_id):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'updateOutline', {
            "cv_id": cv_id
        })

    def importFromPdf(self, file_key):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'importFromPdf', {
            "file_key": file_key
        })

    def importFromDoc(self, file_key):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'importFromDoc', {
            "file_key": file_key
        })

    def reImportFromPdf(self, cv_id):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'reImportFromPdf', {
            "cv_id": cv_id
        })

    def parse(self, cv_id):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'parse', {
            "cv_id": cv_id
        })

    def generate(self, cv_id):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'generate', {
            "cv_id": cv_id
        })

    def obtain(self, cv_id):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'obtain', {
            "cv_id": cv_id
        })

    def mergeCV(self, individual_id, transcript_id):
        """Calls the raet/v10/cv endpoint"""
        return self.api_client.api_request('raet', '10', 'cv', 'mergeCV', {
            "individual_id": individual_id,
            "transcript_id": transcript_id
        })