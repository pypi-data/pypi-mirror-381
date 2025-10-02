from .sip_v10_phone import SipV10Phone
from .sip_v10_call import SipV10Call
from .sip_v10_transcript import SipV10Transcript
from .sip_v10_transcripts import SipV10Transcripts


class SipV10:
    def __init__(self, api_client):
        self.phone = SipV10Phone(api_client)
        self.call = SipV10Call(api_client)
        self.transcript = SipV10Transcript(api_client)
        self.transcripts = SipV10Transcripts(api_client)