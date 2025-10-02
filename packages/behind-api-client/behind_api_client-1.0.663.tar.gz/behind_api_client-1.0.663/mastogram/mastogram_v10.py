from .mastogram_v10_mastodon import MastogramV10Mastodon
from .mastogram_v10_telegram import MastogramV10Telegram
from .mastogram_v10_bluesky import MastogramV10Bluesky


class MastogramV10:
    def __init__(self, api_client):
        self.mastodon = MastogramV10Mastodon(api_client)
        self.telegram = MastogramV10Telegram(api_client)
        self.bluesky = MastogramV10Bluesky(api_client)