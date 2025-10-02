class SalesV20Companies:
    def __init__(self, api_client):
        self.api_client = api_client

    def process(self, queue_id, group_id, account_name, template_name, prompt_id):
        """Calls the sales/v20/companies endpoint"""
        return self.api_client.api_request('sales', '20', 'companies', 'process', {
            "queue_id": queue_id,
            "group_id": group_id,
            "account_name": account_name,
            "template_name": template_name,
            "prompt_id": prompt_id
        })

    def getUnauthorized(self, query, section):
        """Calls the sales/v20/companies endpoint"""
        return self.api_client.api_request('sales', '20', 'companies', 'getUnauthorized', {
            "query": query,
            "section": section
        })