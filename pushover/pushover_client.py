import http.client, urllib, logging
from pushover.pushover_notification import PushoverNotification

class PushoverClient:

    API_URL = "api.pushover.net:443"

    def __init__(self, app_token: str, user_token: str):
        self.app_token = app_token
        self.user_token = user_token

    def send_notification(self, notification: PushoverNotification):
        conn = http.client.HTTPSConnection(self.API_URL)
        conn.request("POST", "/1/messages.json",
            urllib.parse.urlencode({
                "token": self.app_token,
                "user": self.user_token,
                "message": notification.message,
            }), { "Content-type": "application/x-www-form-urlencoded" }
        )
        response = conn.getresponse()
        logging.info("Pushover response: %s" % response.read())
        return response
