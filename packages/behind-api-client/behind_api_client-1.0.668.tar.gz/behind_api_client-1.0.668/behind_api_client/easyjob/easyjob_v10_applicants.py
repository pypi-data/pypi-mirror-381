class EasyjobV10Applicants:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, application_id):
        """Calls the easyjob/v10/applicants endpoint"""
        return self.api_client.api_request('easyjob', '10', 'applicants', 'get', {
            "application_id": application_id
        })

    def stageChange(self, application_id, new_stage):
        """Calls the easyjob/v10/applicants endpoint"""
        return self.api_client.api_request('easyjob', '10', 'applicants', 'stageChange', {
            "application_id": application_id,
            "new_stage": new_stage
        })

    def getList(self, job_description_id):
        """Calls the easyjob/v10/applicants endpoint"""
        return self.api_client.api_request('easyjob', '10', 'applicants', 'getList', {
            "job_description_id": job_description_id
        })