from .easyjob_v10_cv import EasyjobV10Cv
from .easyjob_v10_companies import EasyjobV10Companies
from .easyjob_v10_departments import EasyjobV10Departments
from .easyjob_v10_job_description_artifacts import EasyjobV10JobDescriptionArtifacts
from .easyjob_v10_job_description_candidate_questions import EasyjobV10JobDescriptionCandidateQuestions
from .easyjob_v10_job_descriptions import EasyjobV10JobDescriptions
from .easyjob_v10_candidate_profiles import EasyjobV10CandidateProfiles
from .easyjob_v10_candidate_profile_artifacts import EasyjobV10CandidateProfileArtifacts
from .easyjob_v10_applicants import EasyjobV10Applicants
from .easyjob_v10_applications import EasyjobV10Applications
from .easyjob_v10_reports import EasyjobV10Reports
from .easyjob_v10_answers import EasyjobV10Answers


class EasyjobV10:
    def __init__(self, api_client):
        self.cv = EasyjobV10Cv(api_client)
        self.companies = EasyjobV10Companies(api_client)
        self.departments = EasyjobV10Departments(api_client)
        self.job_description_artifacts = EasyjobV10JobDescriptionArtifacts(api_client)
        self.job_description_candidate_questions = EasyjobV10JobDescriptionCandidateQuestions(api_client)
        self.job_descriptions = EasyjobV10JobDescriptions(api_client)
        self.candidate_profiles = EasyjobV10CandidateProfiles(api_client)
        self.candidate_profile_artifacts = EasyjobV10CandidateProfileArtifacts(api_client)
        self.applicants = EasyjobV10Applicants(api_client)
        self.applications = EasyjobV10Applications(api_client)
        self.reports = EasyjobV10Reports(api_client)
        self.answers = EasyjobV10Answers(api_client)