class EasyjobV10CandidateProfileArtifacts:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, candidate_profile_id, content, source, types):
        """Calls the easyjob/v10/candidateProfileArtifacts endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfileArtifacts', 'create', {
            "candidate_profile_id": candidate_profile_id,
            "content": content,
            "source": source,
            "type": types
        })

    def delete(self, artifact_id):
        """Calls the easyjob/v10/candidateProfileArtifacts endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfileArtifacts', 'delete', {
            "artifact_id": artifact_id
        })

    def getList(self, candidate_profile_id):
        """Calls the easyjob/v10/candidateProfileArtifacts endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfileArtifacts', 'getList', {
            "candidate_profile_id": candidate_profile_id
        })