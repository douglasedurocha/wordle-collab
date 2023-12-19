import json
from asgiref.sync import async_to_sync
from accounts.models import Player  # noqa F401
from .models import Game, Attempt  # noqa F401
from channels.generic.websocket import WebsocketConsumer


class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.game_id = self.scope["url_route"]["kwargs"]["game_id"]
        self.game_group_name = "game_%s" % self.game_id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_name, self.channel_name
        )

    # Receive attempt from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        attempt_word = text_data_json["word"]
        player = text_data_json["player"]

        # player = Player.objects.get(email=player_email)
        # game = Game.objects.get(id=self.game_id)

        # attempt = Attempt(player=player, word=attempt, game=game)
        # attempt.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.game_group_name,
            {"type": "game_attempt", "word": attempt_word, "player": player},
        )

    # Receive attempt from game room
    def game_attempt(self, event):
        attempt_word = event["word"]
        player = event["player"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"word": attempt_word, "player": player}))
