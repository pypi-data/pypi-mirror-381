class EasyjobV10CandidateProfiles:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'create', {})

    def delete(self, profile_id):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'delete', {
            "profile_id": profile_id
        })

    def update(self, profile_id, profile_data):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'update', {
            "profile_id": profile_id,
            "profile_data": profile_data
        })

    def get(self):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'get', {})

    def updateEducation(self, profile_id, education):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'updateEducation', {
            "profile_id": profile_id,
            "education": education
        })

    def updateJobExperience(self, profile_id, job_experience):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'updateJobExperience', {
            "profile_id": profile_id,
            "job_experience": job_experience
        })

    def updateHardSkills(self, profile_id, hard_skills):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'updateHardSkills', {
            "profile_id": profile_id,
            "hard_skills": hard_skills
        })

    def updateSoftSkills(self, profile_id, soft_skills):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'updateSoftSkills', {
            "profile_id": profile_id,
            "soft_skills": soft_skills
        })

    def updateCertificates(self, profile_id, certificates):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'updateCertificates', {
            "profile_id": profile_id,
            "certificates": certificates
        })

    def updateLanguages(self, profile_id, languages):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'updateLanguages', {
            "profile_id": profile_id,
            "languages": languages
        })

    def parseFromPdf(self, url):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'parseFromPdf', {
            "url": url
        })

    def updateStatus(self, profile_id, status):
        """Calls the easyjob/v10/candidateProfiles endpoint"""
        return self.api_client.api_request('easyjob', '10', 'candidateProfiles', 'updateStatus', {
            "profile_id": profile_id,
            "status": status
        })