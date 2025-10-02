class RaetV20Individuals:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, project_id, query, page, page_size):
        """Calls the raet/v20/individuals endpoint"""
        return self.api_client.api_request('raet', '20', 'individuals', 'get', {
            "project_id": project_id,
            "query": query,
            "page": page,
            "page_size": page_size
        })

    def create(self, individual, project_id):
        """Calls the raet/v20/individuals endpoint"""
        return self.api_client.api_request('raet', '20', 'individuals', 'create', {
            "individual": individual,
            "project_id": project_id
        })