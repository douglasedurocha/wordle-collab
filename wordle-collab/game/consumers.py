import json
from asgiref.sync import async_to_sync
from accounts.models import Player
from .models import Game, Attempt
from channels.generic.websocket import WebsocketConsumer
from .wordle import check_word_exists, give_hint


class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.game_id = self.scope["url_route"]["kwargs"]["game_id"]
        self.game_group_name = "game_%s" % self.game_id
        self.player_email = self.scope["user"]

        if not self._check_room_availability():
            self.close()
            return

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_name, self.channel_name
        )
        self.accept()

        game = self._get_game()
        player = self._get_player()
        game.add_player(player)
        game.save()

    def _check_room_availability(self):
        game = self._get_game()
        player = self._get_player()
        max_players = game.max_players

        if game.players_count >= max_players and player not in game.players.all():
            return False

        return True

    def _get_game(self):
        return Game.objects.get(id=self.game_id)

    def _get_player(self):
        return Player.objects.get(email=self.player_email)

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_name, self.channel_name
        )
        game = self._get_game()
        player = self._get_player()
        game.remove_player(player)
        game.save()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        attempt_word = text_data_json["word"].upper()
        player_email = text_data_json["player"]["email"]

        game = self._get_game()
        player = self._get_player()

        if game.is_over:
            return

        if not check_word_exists(attempt_word):
            return

        attempt = Attempt.objects.create(player=player, word=attempt_word, game=game)

        hint = give_hint(attempt_word, game.word)
        attempt.hint = hint

        self._send_attempt(attempt_word, hint, player_email)

        if attempt == game.word:
            game.status = "V"
            game.save()
            return

        elif game.attempts_count >= game.max_attempts:
            game.status = "D"
            game.save()
            return

    def _send_attempt(self, word, hint, player_email):
        async_to_sync(self.channel_layer.group_send)(
            self.game_group_name,
            {
                "type": "attempt",
                "word": word,
                "hint": hint,
                "player": {"email": player_email},
            },
        )

    def attempt(self, event):
        msg_type = "attempt"
        attempt_word = event["word"]
        player_email = event["player"]["email"]
        hint = event["hint"]

        self.send(
            text_data=json.dumps(
                {
                    "msg_type": msg_type,
                    "word": attempt_word,
                    "hint": hint,
                    "player": {"email": player_email},
                }
            )
        )
