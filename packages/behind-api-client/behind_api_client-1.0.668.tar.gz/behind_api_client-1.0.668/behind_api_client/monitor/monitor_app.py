from .monitor_v10 import MonitorV10


class MonitorApp:
    def __init__(self, api_client):
        self.v10 = MonitorV10(api_client)