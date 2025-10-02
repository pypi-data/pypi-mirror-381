class RuKitchenV10SeoArticle:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, page_id):
        """Calls the ru-kitchen/v10/seoArticle endpoint"""
        return self.api_client.api_request('ru-kitchen', '10', 'seoArticle', 'create', {
            "page_id": page_id
        })