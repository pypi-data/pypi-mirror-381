from .tools_v10 import ToolsV10


class ToolsApp:
    def __init__(self, api_client):
        self.v10 = ToolsV10(api_client)