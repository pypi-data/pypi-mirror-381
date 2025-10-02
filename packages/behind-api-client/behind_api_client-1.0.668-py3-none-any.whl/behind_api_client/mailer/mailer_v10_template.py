class MailerV10Template:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, name, body):
        """Calls the mailer/v10/template endpoint"""
        return self.api_client.api_request('mailer', '10', 'template', 'create', {
            "name": name,
            "body": body
        })

    def edit(self, name, body):
        """Calls the mailer/v10/template endpoint"""
        return self.api_client.api_request('mailer', '10', 'template', 'edit', {
            "name": name,
            "body": body
        })