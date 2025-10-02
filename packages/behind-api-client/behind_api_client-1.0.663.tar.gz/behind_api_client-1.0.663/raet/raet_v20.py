from .raet_v20_individuals import RaetV20Individuals
from .raet_v20_cv import RaetV20Cv


class RaetV20:
    def __init__(self, api_client):
        self.individuals = RaetV20Individuals(api_client)
        self.cv = RaetV20Cv(api_client)