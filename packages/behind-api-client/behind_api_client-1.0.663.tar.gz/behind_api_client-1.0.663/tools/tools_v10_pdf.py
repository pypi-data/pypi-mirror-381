class ToolsV10Pdf:
    def __init__(self, api_client):
        self.api_client = api_client

    def toText(self, file_key):
        """Calls the tools/v10/pdf endpoint"""
        return self.api_client.api_request('tools', '10', 'pdf', 'toText', {
            "file_key": file_key
        })

    def toTextFromUrl(self, url):
        """Calls the tools/v10/pdf endpoint"""
        return self.api_client.api_request('tools', '10', 'pdf', 'toTextFromUrl', {
            "url": url
        })

    def renderFromJSON(self, template, data, style):
        """Calls the tools/v10/pdf endpoint"""
        return self.api_client.api_request('tools', '10', 'pdf', 'renderFromJSON', {
            "template": template,
            "data": data,
            "style": style
        })