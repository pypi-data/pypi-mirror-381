class MailerV20Message:
    def __init__(self, api_client):
        self.api_client = api_client

    def send(self, email, recipient_name, reply_to, attachments, account_name, template_name, data, time):
        """Calls the mailer/v20/message endpoint"""
        return self.api_client.api_request('mailer', '20', 'message', 'send', {
            "email": email,
            "recipient_name": recipient_name,
            "reply_to": reply_to,
            "attachments": attachments,
            "account_name": account_name,
            "template_name": template_name,
            "data": data,
            "time": time
        })