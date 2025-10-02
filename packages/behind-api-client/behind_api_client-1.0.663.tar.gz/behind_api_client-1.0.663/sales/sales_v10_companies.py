class SalesV10Companies:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, query, filters, page, page_size, section):
        """Calls the sales/v10/companies endpoint"""
        return self.api_client.api_request('sales', '10', 'companies', 'get', {
            "query": query,
            "filters": filters,
            "page": page,
            "page_size": page_size,
            "section": section
        })

    def getUnauthorized(self):
        """Calls the sales/v10/companies endpoint"""
        return self.api_client.api_request('sales', '10', 'companies', 'getUnauthorized', {})

    def process(self, queue_id, query, filters, account_name, template_name, prompt_id, prompt_title_id):
        """Calls the sales/v10/companies endpoint"""
        return self.api_client.api_request('sales', '10', 'companies', 'process', {
            "queue_id": queue_id,
            "query": query,
            "filters": filters,
            "account_name": account_name,
            "template_name": template_name,
            "prompt_id": prompt_id,
            "prompt_title_id": prompt_title_id
        })

    def crawl(self, queue_id, query, limit):
        """Calls the sales/v10/companies endpoint"""
        return self.api_client.api_request('sales', '10', 'companies', 'crawl', {
            "queue_id": queue_id,
            "query": query,
            "limit": limit
        })

    def test(self, query, filters):
        """Calls the sales/v10/companies endpoint"""
        return self.api_client.api_request('sales', '10', 'companies', 'test', {
            "query": query,
            "filters": filters
        })