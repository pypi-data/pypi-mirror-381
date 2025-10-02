class EasyjobV10Cv:
    def __init__(self, api_client):
        self.api_client = api_client

    def parse(self, content, types):
        """Calls the easyjob/v10/cv endpoint"""
        return self.api_client.api_request('easyjob', '10', 'cv', 'parse', {
            "content": content,
            "type": types
        })