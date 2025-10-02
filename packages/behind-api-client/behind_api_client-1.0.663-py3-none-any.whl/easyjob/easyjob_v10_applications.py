class EasyjobV10Applications:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, candidate_profile_id, job_description_id, message):
        """Calls the easyjob/v10/applications endpoint"""
        return self.api_client.api_request('easyjob', '10', 'applications', 'create', {
            "candidate_profile_id": candidate_profile_id,
            "job_description_id": job_description_id,
            "message": message
        })

    def get(self, job_description_id):
        """Calls the easyjob/v10/applications endpoint"""
        return self.api_client.api_request('easyjob', '10', 'applications', 'get', {
            "job_description_id": job_description_id
        })

    def getQuestions(self, job_description_id, category):
        """Calls the easyjob/v10/applications endpoint"""
        return self.api_client.api_request('easyjob', '10', 'applications', 'getQuestions', {
            "job_description_id": job_description_id,
            "category": category
        })

    def getUnansweredQuestionsList(self, application_id, limit):
        """Calls the easyjob/v10/applications endpoint"""
        return self.api_client.api_request('easyjob', '10', 'applications', 'getUnansweredQuestionsList', {
            "application_id": application_id,
            "limit": limit
        })