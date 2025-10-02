class SipV10Call:
    def __init__(self, api_client):
        self.api_client = api_client

    def createIntent(self, phone_number, meta):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'createIntent', {
            "phone_number": phone_number,
            "meta": meta
        })

    def getIntent(self, phone_1, phone_2):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'getIntent', {
            "phone_1": phone_1,
            "phone_2": phone_2
        })

    def transcribe(self, call_id):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'transcribe', {
            "call_id": call_id
        })

    def transcribeAsync(self, call_id):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'transcribeAsync', {
            "call_id": call_id
        })

    def transcribeLiveDemo(self, call_id):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'transcribeLiveDemo', {
            "call_id": call_id
        })

    def transcribeLive(self, call_id):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'transcribeLive', {
            "call_id": call_id
        })

    def extractCVInsights(self, call_id, cv_id):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'extractCVInsights', {
            "call_id": call_id,
            "cv_id": cv_id
        })

    def extractJDInsights(self, call_id, project_id):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'extractJDInsights', {
            "call_id": call_id,
            "project_id": project_id
        })

    def extractReportInsights(self, call_id, cv_id):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'extractReportInsights', {
            "call_id": call_id,
            "cv_id": cv_id
        })

    def transcribeLiveCallback(self, extended, data):
        """Calls the sip/v10/call endpoint"""
        return self.api_client.api_request('sip', '10', 'call', 'transcribeLiveCallback', {
            "extended": extended,
            "data": data
        })