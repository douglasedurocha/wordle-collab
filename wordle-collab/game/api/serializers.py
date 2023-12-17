from game.models import Game
from rest_framework.serializers import ModelSerializer


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ("id", "players", "status")
