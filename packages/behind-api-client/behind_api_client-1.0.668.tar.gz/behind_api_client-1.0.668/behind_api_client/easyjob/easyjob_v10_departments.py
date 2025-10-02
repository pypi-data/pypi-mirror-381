class EasyjobV10Departments:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, company_id, name):
        """Calls the easyjob/v10/departments endpoint"""
        return self.api_client.api_request('easyjob', '10', 'departments', 'create', {
            "company_id": company_id,
            "name": name
        })

    def delete(self, department_id):
        """Calls the easyjob/v10/departments endpoint"""
        return self.api_client.api_request('easyjob', '10', 'departments', 'delete', {
            "department_id": department_id
        })

    def update(self, department_id, name):
        """Calls the easyjob/v10/departments endpoint"""
        return self.api_client.api_request('easyjob', '10', 'departments', 'update', {
            "department_id": department_id,
            "name": name
        })

    def getList(self, company_id):
        """Calls the easyjob/v10/departments endpoint"""
        return self.api_client.api_request('easyjob', '10', 'departments', 'getList', {
            "company_id": company_id
        })