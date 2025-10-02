class SipV10Transcript:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, transcript_id):
        """Calls the sip/v10/transcript endpoint"""
        return self.api_client.api_request('sip', '10', 'transcript', 'get', {
            "transcript_id": transcript_id
        })

    def deleteUpdates(self, transcript_id):
        """Calls the sip/v10/transcript endpoint"""
        return self.api_client.api_request('sip', '10', 'transcript', 'deleteUpdates', {
            "transcript_id": transcript_id
        })