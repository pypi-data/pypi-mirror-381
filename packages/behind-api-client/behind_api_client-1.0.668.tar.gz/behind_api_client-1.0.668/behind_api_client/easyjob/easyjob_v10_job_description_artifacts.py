class EasyjobV10JobDescriptionArtifacts:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, job_description_id, content):
        """Calls the easyjob/v10/jobDescriptionArtifacts endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionArtifacts', 'create', {
            "job_description_id": job_description_id,
            "content": content
        })

    def delete(self, artifact_id):
        """Calls the easyjob/v10/jobDescriptionArtifacts endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionArtifacts', 'delete', {
            "artifact_id": artifact_id
        })

    def getList(self, job_description_id):
        """Calls the easyjob/v10/jobDescriptionArtifacts endpoint"""
        return self.api_client.api_request('easyjob', '10', 'jobDescriptionArtifacts', 'getList', {
            "job_description_id": job_description_id
        })