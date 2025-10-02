class RuKitchenV10Importer:
    def __init__(self, api_client):
        self.api_client = api_client

    def extractIngredients(self, page_id):
        """Calls the ru-kitchen/v10/importer endpoint"""
        return self.api_client.api_request('ru-kitchen', '10', 'importer', 'extractIngredients', {
            "page_id": page_id
        })

    def fetchFDC(self, name):
        """Calls the ru-kitchen/v10/importer endpoint"""
        return self.api_client.api_request('ru-kitchen', '10', 'importer', 'fetchFDC', {
            "name": name
        })

    def fetchIngredient(self, name, recipe):
        """Calls the ru-kitchen/v10/importer endpoint"""
        return self.api_client.api_request('ru-kitchen', '10', 'importer', 'fetchIngredient', {
            "name": name,
            "recipe": recipe
        })