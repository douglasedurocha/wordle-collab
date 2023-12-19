from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer, AttemptSerializer
from game.models import Game, Attempt


class GameCreateView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        game = Game.objects.create(word="teste")
        game.add_player(request.user)
        return Response(GameSerializer(game).data, status=201)


class GetGameView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, game_id):
        game = Game.objects.get(id=game_id)
        return Response(GameSerializer(game).data, status=200)


class GetAttemptView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, game_id):
        attempts = Attempt.objects.filter(game=game_id)
        return Response(AttemptSerializer(attempts, many=True).data, status=200)


class OpenGameListView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request):
        games = Game.objects.filter(status="W")
        return Response(GameSerializer(games, many=True).data, status=200)
