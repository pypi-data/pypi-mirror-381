class RaetV10Jd:
    def __init__(self, api_client):
        self.api_client = api_client

    def update(self, project_id, jd):
        """Calls the raet/v10/jd endpoint"""
        return self.api_client.api_request('raet', '10', 'jd', 'update', {
            "project_id": project_id,
            "jd": jd
        })

    def updateSys(self, project_id, jd):
        """Calls the raet/v10/jd endpoint"""
        return self.api_client.api_request('raet', '10', 'jd', 'updateSys', {
            "project_id": project_id,
            "jd": jd
        })

    def parse(self, project_id, data):
        """Calls the raet/v10/jd endpoint"""
        return self.api_client.api_request('raet', '10', 'jd', 'parse', {
            "project_id": project_id,
            "data": data
        })

    def parseSys(self, project_id, data):
        """Calls the raet/v10/jd endpoint"""
        return self.api_client.api_request('raet', '10', 'jd', 'parseSys', {
            "project_id": project_id,
            "data": data
        })

    def parseFromThePhoneCall(self, project_id, call_id):
        """Calls the raet/v10/jd endpoint"""
        return self.api_client.api_request('raet', '10', 'jd', 'parseFromThePhoneCall', {
            "project_id": project_id,
            "call_id": call_id
        })