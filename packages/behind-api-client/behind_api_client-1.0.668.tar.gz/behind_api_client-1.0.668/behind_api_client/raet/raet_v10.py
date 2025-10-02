from .raet_v10_project import RaetV10Project
from .raet_v10_projects import RaetV10Projects
from .raet_v10_jd import RaetV10Jd
from .raet_v10_cv import RaetV10Cv
from .raet_v10_individuals import RaetV10Individuals
from .raet_v10_individual import RaetV10Individual
from .raet_v10_report import RaetV10Report


class RaetV10:
    def __init__(self, api_client):
        self.project = RaetV10Project(api_client)
        self.projects = RaetV10Projects(api_client)
        self.jd = RaetV10Jd(api_client)
        self.cv = RaetV10Cv(api_client)
        self.individuals = RaetV10Individuals(api_client)
        self.individual = RaetV10Individual(api_client)
        self.report = RaetV10Report(api_client)