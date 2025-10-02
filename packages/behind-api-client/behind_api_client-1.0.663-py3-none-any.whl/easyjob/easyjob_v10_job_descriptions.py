class EasyjobV10JobDescriptions:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, department_id, title, description):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'create', {
            "department_id": department_id,
            "title": title,
            "description": description
        })

    def delete(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'delete', {
            "job_description_id": job_description_id
        })

    def close(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'close', {
            "job_description_id": job_description_id
        })

    def update(self, job_description_id, title, description, published_at, deadline_at):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'update', {
            "job_description_id": job_description_id,
            "title": title,
            "description": description,
            "published_at": published_at,
            "deadline_at": deadline_at
        })

    def updateData(self, job_description_id, data):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'updateData', {
            "job_description_id": job_description_id,
            "data": data
        })

    def getList(self, department_id):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'getList', {
            "department_id": department_id
        })

    def get(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'get', {
            "job_description_id": job_description_id
        })

    def publish(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'publish', {
            "job_description_id": job_description_id
        })

    def getUnauthorised(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'getUnauthorised', {
            "job_description_id": job_description_id
        })

    def textUpdate(self, job_description_id, text):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'textUpdate', {
            "job_description_id": job_description_id,
            "text": text
        })

    def updateStatus(self, job_description_id, status):
        """Calls the easyjob/v10/jobDescriptions endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptions', 'updateStatus', {
            "job_description_id": job_description_id,
            "status": status
        })