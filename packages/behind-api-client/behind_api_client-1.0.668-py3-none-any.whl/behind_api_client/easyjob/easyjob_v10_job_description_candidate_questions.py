class EasyjobV10JobDescriptionCandidateQuestions:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, job_description_id, question, types, weight, category):
        """Calls the easyjob/v10/jobDescriptionCandidateQuestions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionCandidateQuestions', 'create', {
            "job_description_id": job_description_id,
            "question": question,
            "type": types,
            "weight": weight,
            "category": category
        })

    def delete(self, question_id):
        """Calls the easyjob/v10/jobDescriptionCandidateQuestions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionCandidateQuestions', 'delete', {
            "question_id": question_id
        })

    def deleteAll(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptionCandidateQuestions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionCandidateQuestions', 'deleteAll', {
            "job_description_id": job_description_id
        })

    def getList(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptionCandidateQuestions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionCandidateQuestions', 'getList', {
            "job_description_id": job_description_id
        })

    def getByCategory(self, job_description_id, category):
        """Calls the easyjob/v10/jobDescriptionCandidateQuestions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionCandidateQuestions', 'getByCategory', {
            "job_description_id": job_description_id,
            "category": category
        })

    def edit(self, question_id, text, weight):
        """Calls the easyjob/v10/jobDescriptionCandidateQuestions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionCandidateQuestions', 'edit', {
            "question_id": question_id,
            "text": text,
            "weight": weight
        })

    def extract(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptionCandidateQuestions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionCandidateQuestions', 'extract', {
            "job_description_id": job_description_id
        })