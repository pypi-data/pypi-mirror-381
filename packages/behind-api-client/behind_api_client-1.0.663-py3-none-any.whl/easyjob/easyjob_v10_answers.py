class EasyjobV10Answers:
    def __init__(self, api_client):
        self.api_client = api_client

    def store(self, user_id, application_id, answers):
        """Calls the easyjob/v10/answers endpoint"""
        return self.api_client.api_request('easyjob', '10', 'answers', 'store', {
            "user_id": user_id,
            "application_id": application_id,
            "answers": answers
        })