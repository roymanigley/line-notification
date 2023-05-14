import json
from urllib.error import HTTPError

from flask import Flask, request, Response
from waitress import serve

from line.LineClient import LineClient

__app__ = Flask(__name__)
__line_client__ = LineClient()


@__app__.route("/")
def root():
    return create_response({
        "application": "line-notification",
        "available resources": [
                {
                    "method": "GET",
                    "route": "/api/send_message",
                    "parameters": [
                        {"name": "message"}
                    ]
                }
            ]
        }, 200)


@__app__.route('/api/send_message')
def __send_message__():
    message = request.args.get('message')
    print("[+] sending broadcast message: {}", message)
    if message is None or message == '':
        return create_response({"status": "error", "message": "the parameter 'message' is not set"})
    try:
        __line_client__.send_broadcast_message(message)
        return create_response({"status": "success", "message": "broadcast message sent successfully"})
    except HTTPError as e:
        print("[!] sending broadcast message failed: {}", str(e))
        return create_response({"status": "error", "message": str(e)}, e.code)
    except Exception as e:
        print("[!] sending broadcast message failed: {}", str(e))
        return create_response({"status": "error", "message": str(e)}, 500)


@__app__.errorhandler(404)
def page_not_found(e):
    return create_response({"status": "error", "message": "resource not found"}, 404)


def create_response(message: dict, status=200, mimetype="application/json"):
    return Response(json.dumps(message), status=status, mimetype=mimetype)


class Server(object):

    def __init__(self, host="0.0.0.0", port=8000):
        self.host = host
        self.port = port

    def start(self, ) -> None:
        print("[+] server started {}:{}".format(self.host, self.port))
        serve(__app__, host=self.host, port=self.port)
