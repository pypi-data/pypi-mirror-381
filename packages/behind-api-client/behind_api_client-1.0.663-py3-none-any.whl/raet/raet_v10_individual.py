class RaetV10Individual:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, individual_id):
        """Calls the raet/v10/individual endpoint"""
        return self.api_client.api_request('raet', '10', 'individual', 'get', {
            "individual_id": individual_id
        })

    def getByPhoneNumber(self, phone_number):
        """Calls the raet/v10/individual endpoint"""
        return self.api_client.api_request('raet', '10', 'individual', 'getByPhoneNumber', {
            "phone_number": phone_number
        })

    def update(self, individual_id, individual):
        """Calls the raet/v10/individual endpoint"""
        return self.api_client.api_request('raet', '10', 'individual', 'update', {
            "individual_id": individual_id,
            "individual": individual
        })

    def contactsGet(self, individual_id):
        """Calls the raet/v10/individual endpoint"""
        return self.api_client.api_request('raet', '10', 'individual', 'contactsGet', {
            "individual_id": individual_id
        })

    def delete(self, individual_id):
        """Calls the raet/v10/individual endpoint"""
        return self.api_client.api_request('raet', '10', 'individual', 'delete', {
            "individual_id": individual_id
        })