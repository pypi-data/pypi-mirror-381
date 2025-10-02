class ChatV20Message:
    def __init__(self, api_client):
        self.api_client = api_client

    def create(self, chat_uuid, text, headline, types):
        """Calls the chat/v20/message endpoint"""
        return self.api_client.api_request('chat', '20', 'message', 'create', {
            "chat_uuid": chat_uuid,
            "text": text,
            "headline": headline,
            "type": types
        })

    def render(self, chat_uuid, prompt, headlinePrompt, extended):
        """Calls the chat/v20/message endpoint"""
        return self.api_client.api_request('chat', '20', 'message', 'render', {
            "chat_uuid": chat_uuid,
            "prompt": prompt,
            "headlinePrompt": headlinePrompt,
            "extended": extended
        })