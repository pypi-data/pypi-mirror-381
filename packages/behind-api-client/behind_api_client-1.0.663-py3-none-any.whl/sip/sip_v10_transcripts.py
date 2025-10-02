class SipV10Transcripts:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self):
        """Calls the sip/v10/transcripts endpoint"""
        return self.api_client.api_request('sip', '10', 'transcripts', 'get', {})

    def getByIndividualId(self, individual_id):
        """Calls the sip/v10/transcripts endpoint"""
        return self.api_client.api_request('sip', '10', 'transcripts', 'getByIndividualId', {
            "individual_id": individual_id
        })