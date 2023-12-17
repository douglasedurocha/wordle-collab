from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer
from game.models import Game


class GameCreateView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        game = Game.objects.create(word="teste")
        game.add_player(request.user)
        return Response(GameSerializer(game).data, status=201)
