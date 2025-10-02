class RaetV10Individuals:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, query, page, page_size):
        """Calls the raet/v10/individuals endpoint"""
        return self.api_client.api_request('raet', '10', 'individuals', 'get', {
            "query": query,
            "page": page,
            "page_size": page_size
        })

    def getByPhoneNumber(self, phone_number):
        """Calls the raet/v10/individuals endpoint"""
        return self.api_client.api_request('raet', '10', 'individuals', 'getByPhoneNumber', {
            "phone_number": phone_number
        })

    def getByPhoneNumberSystem(self, phone_number, user_id):
        """Calls the raet/v10/individuals endpoint"""
        return self.api_client.api_request('raet', '10', 'individuals', 'getByPhoneNumberSystem', {
            "phone_number": phone_number,
            "user_id": user_id
        })

    def create(self, individual):
        """Calls the raet/v10/individuals endpoint"""
        return self.api_client.api_request('raet', '10', 'individuals', 'create', {
            "individual": individual
        })