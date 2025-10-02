class MailerV10Settings:
    def __init__(self, api_client):
        self.api_client = api_client

    def update(self, name, smtp_from_name, smtp_user, smtp_server, smtp_port, smtp_password):
        """Calls the mailer/v10/settings endpoint"""
        return self.api_client.api_request('mailer', '10', 'settings', 'update', {
            "name": name,
            "smtp_from_name": smtp_from_name,
            "smtp_user": smtp_user,
            "smtp_server": smtp_server,
            "smtp_port": smtp_port,
            "smtp_password": smtp_password
        })

    def updateImap(self, name, imap_user, imap_server, imap_port, imap_password):
        """Calls the mailer/v10/settings endpoint"""
        return self.api_client.api_request('mailer', '10', 'settings', 'updateImap', {
            "name": name,
            "imap_user": imap_user,
            "imap_server": imap_server,
            "imap_port": imap_port,
            "imap_password": imap_password
        })

    def get(self, name):
        """Calls the mailer/v10/settings endpoint"""
        return self.api_client.api_request('mailer', '10', 'settings', 'get', {
            "name": name
        })

    def getImap(self, name):
        """Calls the mailer/v10/settings endpoint"""
        return self.api_client.api_request('mailer', '10', 'settings', 'getImap', {
            "name": name
        })