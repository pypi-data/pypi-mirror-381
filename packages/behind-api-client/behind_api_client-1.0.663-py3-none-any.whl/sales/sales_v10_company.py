class SalesV10Company:
    def __init__(self, api_client):
        self.api_client = api_client

    def get(self, object_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'get', {
            "object_id": object_id
        })

    def getUnauthorised(self, object_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'getUnauthorised', {
            "object_id": object_id
        })

    def contactsGet(self, object_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'contactsGet', {
            "object_id": object_id
        })

    def process(self, object_id, queue_id, account_name, template_name, prompt_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'process', {
            "object_id": object_id,
            "queue_id": queue_id,
            "account_name": account_name,
            "template_name": template_name,
            "prompt_id": prompt_id
        })

    def getProgressStatus(self, object_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'getProgressStatus', {
            "object_id": object_id
        })

    def parseSite(self, object_id, queue_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'parseSite', {
            "object_id": object_id,
            "queue_id": queue_id
        })

    def parser(self, object_id, emails):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'parser', {
            "object_id": object_id,
            "emails": emails
        })

    def emailUpdate(self, object_id, emails):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'emailUpdate', {
            "object_id": object_id,
            "emails": emails
        })

    def updateDescription(self, object_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'updateDescription', {
            "object_id": object_id
        })

    def crawlerStatusUpdate(self, object_id, data):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'crawlerStatusUpdate', {
            "object_id": object_id,
            "data": data
        })

    def emailSend(self, object_id, account_name, template_name, prompt_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'emailSend', {
            "object_id": object_id,
            "account_name": account_name,
            "template_name": template_name,
            "prompt_id": prompt_id
        })

    def promptRender(self, object_id, prompt_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'promptRender', {
            "object_id": object_id,
            "prompt_id": prompt_id
        })

    def notes(self, object_id):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'notes', {
            "object_id": object_id
        })

    def add(self, name, country, website, category):
        """Calls the sales/v10/company endpoint"""
        return self.api_client.api_request('sales', '10', 'company', 'add', {
            "name": name,
            "country": country,
            "website": website,
            "category": category
        })