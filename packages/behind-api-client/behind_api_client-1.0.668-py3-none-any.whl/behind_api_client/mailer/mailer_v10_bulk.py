class MailerV10Bulk:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, node_name, template_name, account_name, body, headline, data, time, filters):
        """Calls the mailer/v10/bulk endpoint"""
        return self.api_client.api_request('mailer', '10', 'bulk', 'create', {
            "node_name": node_name,
            "template_name": template_name,
            "account_name": account_name,
            "body": body,
            "headline": headline,
            "data": data,
            "time": time,
            "filters": filters
        })