class GptV30Chat:
    def __init__(self, api_client):
        self.api_client = api_client

    def execute(self, messages, options, context, prompt, reverseSystem, jsonSchema):
        """Calls the gpt/v30/chat endpoint"""
        return self.api_client.api_request('gpt', '30', 'chat', 'execute', {
            "messages": messages,
            "options": options,
            "context": context,
            "prompt": prompt,
            "reverseSystem": reverseSystem,
            "jsonSchema": jsonSchema
        })