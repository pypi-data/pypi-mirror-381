from .tools_v10_pdf import ToolsV10Pdf


class ToolsV10:
    def __init__(self, api_client):
        self.pdf = ToolsV10Pdf(api_client)