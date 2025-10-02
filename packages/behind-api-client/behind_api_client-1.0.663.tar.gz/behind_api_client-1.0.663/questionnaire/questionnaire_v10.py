from .questionnaire_v10_form import QuestionnaireV10Form


class QuestionnaireV10:
    def __init__(self, api_client):
        self.form = QuestionnaireV10Form(api_client)