import os
import uuid
from urllib.request import Request, urlopen

__API_URL__ = "https://api.line.me/v2"
__API_TOKEN__ = os.environ.get("LINE_API_TOKEN")


class LineClient(object):

    def __init__(self):
        if __API_TOKEN__ is None:
            raise Exception("missing ENV VARIABLE: LINE_API_TOKEN")
        self.token = __API_TOKEN__

    def send_broadcast_message(self, message):
        headers = {
            "Content-Type": "application/json",
            "X-Line-Retry-Key": str(uuid.uuid1()),
            "Authorization": "Bearer {}".format(self.token)
        }
        payload = '{ "messages": [ { "type": "text", "text": "' + message.replace('"', '\\"') + '" } ] }'
        r = Request(__API_URL__ + "/bot/message/broadcast", headers=headers, method="POST", data=payload.encode())
        urlopen(r)

