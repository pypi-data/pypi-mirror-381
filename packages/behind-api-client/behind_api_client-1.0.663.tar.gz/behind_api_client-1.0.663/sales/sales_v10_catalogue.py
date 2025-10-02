class SalesV10Catalogue:
    def __init__(self, api_client):
        self.api_client = api_client

    def getRecords(self, page_size, section):
        """Calls the sales/v10/catalogue endpoint"""
        return self.api_client.api_request('sales', '10', 'catalogue', 'getRecords', {
            "page_size": page_size,
            "section": section
        })

    def getAllRecords(self, section):
        """Calls the sales/v10/catalogue endpoint"""
        return self.api_client.api_request('sales', '10', 'catalogue', 'getAllRecords', {
            "section": section
        })

    def getAllArticles(self, country):
        """Calls the sales/v10/catalogue endpoint"""
        return self.api_client.api_request('sales', '10', 'catalogue', 'getAllArticles', {
            "country": country
        })

    def getRecord(self, object_id):
        """Calls the sales/v10/catalogue endpoint"""
        return self.api_client.api_request('sales', '10', 'catalogue', 'getRecord', {
            "object_id": object_id
        })

    def getArticle(self, municipality, branch):
        """Calls the sales/v10/catalogue endpoint"""
        return self.api_client.api_request('sales', '10', 'catalogue', 'getArticle', {
            "municipality": municipality,
            "branch": branch
        })

    def getMunicipalities(self, country):
        """Calls the sales/v10/catalogue endpoint"""
        return self.api_client.api_request('sales', '10', 'catalogue', 'getMunicipalities', {
            "country": country
        })

    def getArticles(self, municipality):
        """Calls the sales/v10/catalogue endpoint"""
        return self.api_client.api_request('sales', '10', 'catalogue', 'getArticles', {
            "municipality": municipality
        })