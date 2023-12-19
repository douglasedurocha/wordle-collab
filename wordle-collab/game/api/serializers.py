from accounts.models import Player
from game.models import Game, Attempt
from rest_framework.serializers import ModelSerializer


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "id",
            "players",
            "status",
            "max_players",
            "players_count",
            "author_email",
            "attempts_count",
        )


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = (
            "id",
            "email",
        )


class AttemptSerializer(ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = Attempt
        fields = (
            "id",
            "player",
            "word",
            "hint",
            "game",
        )
