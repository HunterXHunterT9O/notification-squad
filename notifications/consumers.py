from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from django.contrib.auth.models import User

class NotificationConsumer(WebsocketConsumer):
    
    def connect(self):
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        #self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            'notifications',
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            'notifications',
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        
        sender = User.objects.get(pk=text_data_json['userPk'])
        notification = utils.generate_notification(text_data_json['action'])
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': sender.username,
                'pk': text_data_json['userPk']
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'username': event['username'],
            'pk': event['pk']
        }))
