from cgitb import text
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    room_group_name = "default"
    def connect(self):
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()


    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        text_json_data = json.loads(text_data)
        # if "name" in text_json_data:
        #     name = text_json_data["name"]
        #     msg = f"{name} has entered the chat"
        #     print(msg)
        # else:
        msg =  text_json_data["message"]
        name = text_json_data["username"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':msg,
                'username':name,
                
            }
        )
    
    def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username':username 
        }))
