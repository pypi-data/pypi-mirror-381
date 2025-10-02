from .monitor_v10_records import MonitorV10Records
from .monitor_v10_record import MonitorV10Record
from .monitor_v10_finances import MonitorV10Finances


class MonitorV10:
    def __init__(self, api_client):
        self.records = MonitorV10Records(api_client)
        self.record = MonitorV10Record(api_client)
        self.finances = MonitorV10Finances(api_client)