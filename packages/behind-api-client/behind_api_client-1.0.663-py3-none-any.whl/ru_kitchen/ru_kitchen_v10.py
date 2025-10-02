from .ru_kitchen_v10_importer import RuKitchenV10Importer
from .ru_kitchen_v10_seo_article import RuKitchenV10SeoArticle


class RuKitchenV10:
    def __init__(self, api_client):
        self.importer = RuKitchenV10Importer(api_client)
        self.seo_article = RuKitchenV10SeoArticle(api_client)