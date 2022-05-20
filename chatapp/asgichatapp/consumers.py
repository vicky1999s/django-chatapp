import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps(
            {"chat": "its working"}
        ))

    def receive(self, text_data=None, bytes_data=None):
        text_json_data = json.loads(text_data)
        msg =  text_json_data["message"]
        print(msg)
        self.send(text_data=json.dumps(
            {
                "type": "chat",
                "message": msg
            }
        ))
