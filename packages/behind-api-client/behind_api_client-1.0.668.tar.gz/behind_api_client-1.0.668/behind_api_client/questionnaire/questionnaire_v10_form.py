class QuestionnaireV10Form:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, form_id):
        """Calls the questionnaire/v10/form endpoint"""
        return self.api_client.api_request('questionnaire', '10', 'form', 'get', {
            "form_id": form_id
        })

    def send(self, form_id, data):
        """Calls the questionnaire/v10/form endpoint"""
        return self.api_client.api_request('questionnaire', '10', 'form', 'send', {
            "form_id": form_id,
            "data": data
        })