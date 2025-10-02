from .questionnaire_v10 import QuestionnaireV10


class QuestionnaireApp:
    def __init__(self, api_client):
        self.v10 = QuestionnaireV10(api_client)