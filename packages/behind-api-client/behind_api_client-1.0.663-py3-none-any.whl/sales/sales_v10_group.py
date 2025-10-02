class SalesV10Group:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, group_id, page, page_size):
        """Calls the sales/v10/group endpoint"""
        return self.api_client.api_request('sales', '10', 'group', 'get', {
            "group_id": group_id,
            "page": page,
            "page_size": page_size
        })

    def lists(self, group_id):
        """Calls the sales/v10/group endpoint"""
        return self.api_client.api_request('sales', '10', 'group', 'lists', {
            "group_id": group_id
        })

    def delete(self, group_id):
        """Calls the sales/v10/group endpoint"""
        return self.api_client.api_request('sales', '10', 'group', 'delete', {
            "group_id": group_id
        })

    def rename(self, group_id, name):
        """Calls the sales/v10/group endpoint"""
        return self.api_client.api_request('sales', '10', 'group', 'rename', {
            "group_id": group_id,
            "name": name
        })

    def companyAdd(self, group_id, company_id):
        """Calls the sales/v10/group endpoint"""
        return self.api_client.api_request('sales', '10', 'group', 'companyAdd', {
            "group_id": group_id,
            "company_id": company_id
        })

    def companiesAdd(self, group_id, companies):
        """Calls the sales/v10/group endpoint"""
        return self.api_client.api_request('sales', '10', 'group', 'companiesAdd', {
            "group_id": group_id,
            "companies": companies
        })

    def companyDelete(self, group_id, company_id):
        """Calls the sales/v10/group endpoint"""
        return self.api_client.api_request('sales', '10', 'group', 'companyDelete', {
            "group_id": group_id,
            "company_id": company_id
        })

    def companiesDelete(self, group_id, companies):
        """Calls the sales/v10/group endpoint"""
        return self.api_client.api_request('sales', '10', 'group', 'companiesDelete', {
            "group_id": group_id,
            "companies": companies
        })