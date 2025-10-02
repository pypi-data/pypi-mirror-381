class MailerV10Message:
    def __init__(self, api_client):
        self.api_client = api_client

    def send(self, email, recipient_name, account_name, template_name, data, time):
        """Calls the mailer/v10/message endpoint"""
        return self.api_client.api_request('mailer', '10', 'message', 'send', {
            "email": email,
            "recipient_name": recipient_name,
            "account_name": account_name,
            "template_name": template_name,
            "data": data,
            "time": time
        })

    def sendTo(self, user_key, account_name, template_name, data, time):
        """Calls the mailer/v10/message endpoint"""
        return self.api_client.api_request('mailer', '10', 'message', 'sendTo', {
            "user_key": user_key,
            "account_name": account_name,
            "template_name": template_name,
            "data": data,
            "time": time
        })

    def sendMsg(self, email, recipient_name, account_name, template_name, msg_name, data, time):
        """Calls the mailer/v10/message endpoint"""
        return self.api_client.api_request('mailer', '10', 'message', 'sendMsg', {
            "email": email,
            "recipient_name": recipient_name,
            "account_name": account_name,
            "template_name": template_name,
            "msg_name": msg_name,
            "data": data,
            "time": time
        })

    def sendMsgTo(self, user_key, account_name, template_name, msg_name, data, time):
        """Calls the mailer/v10/message endpoint"""
        return self.api_client.api_request('mailer', '10', 'message', 'sendMsgTo', {
            "user_key": user_key,
            "account_name": account_name,
            "template_name": template_name,
            "msg_name": msg_name,
            "data": data,
            "time": time
        })

    def get(self, message_id):
        """Calls the mailer/v10/message endpoint"""
        return self.api_client.api_request('mailer', '10', 'message', 'get', {
            "message_id": message_id
        })

    def track(self, message_id):
        """Calls the mailer/v10/message endpoint"""
        return self.api_client.api_request('mailer', '10', 'message', 'track', {
            "message_id": message_id
        })

    def getStatus(self, message_id):
        """Calls the mailer/v10/message endpoint"""
        return self.api_client.api_request('mailer', '10', 'message', 'getStatus', {
            "message_id": message_id
        })

    def listGet(self):
        """Calls the mailer/v10/message endpoint"""
        return self.api_client.api_request('mailer', '10', 'message', 'listGet', {})