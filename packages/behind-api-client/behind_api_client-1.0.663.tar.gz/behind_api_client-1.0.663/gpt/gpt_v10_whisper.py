class GptV10Whisper:
    def __init__(self, api_client):
        self.api_client = api_client

    def transcribe(self, file_name):
        """Calls the gpt/v10/whisper endpoint"""
        return self.api_client.api_request('gpt', '10', 'whisper', 'transcribe', {
            "file_name": file_name
        })

    def transcribeLive(self, file_name, callback, extended):
        """Calls the gpt/v10/whisper endpoint"""
        return self.api_client.api_request('gpt', '10', 'whisper', 'transcribeLive', {
            "file_name": file_name,
            "callback": callback,
            "extended": extended
        })