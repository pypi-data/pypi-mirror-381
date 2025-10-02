from .ru_kitchen_v10 import RuKitchenV10


class RuKitchenApp:
    def __init__(self, api_client):
        self.v10 = RuKitchenV10(api_client)