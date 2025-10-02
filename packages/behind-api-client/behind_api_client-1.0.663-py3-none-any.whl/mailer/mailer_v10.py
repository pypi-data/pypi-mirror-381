from .mailer_v10_message import MailerV10Message
from .mailer_v10_settings import MailerV10Settings
from .mailer_v10_template import MailerV10Template
from .mailer_v10_bulk import MailerV10Bulk


class MailerV10:
    def __init__(self, api_client):
        self.message = MailerV10Message(api_client)
        self.settings = MailerV10Settings(api_client)
        self.template = MailerV10Template(api_client)
        self.bulk = MailerV10Bulk(api_client)