class SipV10Phone:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, phone_number):
        """Calls the sip/v10/phone endpoint"""
        return self.api_client.api_request('sip', '10', 'phone', 'create', {
            "phone_number": phone_number
        })

    def getUser(self, phone_number):
        """Calls the sip/v10/phone endpoint"""
        return self.api_client.api_request('sip', '10', 'phone', 'getUser', {
            "phone_number": phone_number
        })

    def getContactName(self, phone_number, caller_id):
        """Calls the sip/v10/phone endpoint"""
        return self.api_client.api_request('sip', '10', 'phone', 'getContactName', {
            "phone_number": phone_number,
            "caller_id": caller_id
        })

    def getContactNameText(self, phone_number, caller_id):
        """Calls the sip/v10/phone endpoint"""
        return self.api_client.api_request('sip', '10', 'phone', 'getContactNameText', {
            "phone_number": phone_number,
            "caller_id": caller_id
        })

    def getWebRTCCredentials(self):
        """Calls the sip/v10/phone endpoint"""
        return self.api_client.api_request('sip', '10', 'phone', 'getWebRTCCredentials', {})