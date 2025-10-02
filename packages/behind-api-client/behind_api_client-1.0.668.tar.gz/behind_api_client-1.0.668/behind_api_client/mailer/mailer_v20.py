from .mailer_v20_message import MailerV20Message


class MailerV20:
    def __init__(self, api_client):
        self.message = MailerV20Message(api_client)