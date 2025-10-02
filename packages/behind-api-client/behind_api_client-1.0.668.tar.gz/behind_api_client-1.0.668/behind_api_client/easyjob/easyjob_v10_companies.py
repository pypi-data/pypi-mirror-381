class EasyjobV10Companies:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, name):
        """Calls the easyjob/v10/companies endpoint"""
        return self.api_client.api_request('easyjob', '10', 'companies', 'create', {
            "name": name
        })

    def delete(self, company_id):
        """Calls the easyjob/v10/companies endpoint"""
        return self.api_client.api_request('easyjob', '10', 'companies', 'delete', {
            "company_id": company_id
        })

    def update(self, company_id, name):
        """Calls the easyjob/v10/companies endpoint"""
        return self.api_client.api_request('easyjob', '10', 'companies', 'update', {
            "company_id": company_id,
            "name": name
        })

    def getList(self):
        """Calls the easyjob/v10/companies endpoint"""
        return self.api_client.api_request('easyjob', '10', 'companies', 'getList', {})