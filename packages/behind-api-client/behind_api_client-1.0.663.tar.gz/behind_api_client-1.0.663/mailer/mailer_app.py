from .mailer_v10 import MailerV10
from .mailer_v20 import MailerV20


class MailerApp:
    def __init__(self, api_client):
        self.v10 = MailerV10(api_client)
        self.v20 = MailerV20(api_client)