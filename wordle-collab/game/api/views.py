from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GameSerializer, AttemptSerializer
from game.models import Game, Attempt
from wordle.wordle import generate_random_word


class GameView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        word = generate_random_word()
        game = Game.objects.create(word=word)
        game.add_player(request.user)
        game.save()
        return Response(GameSerializer(game).data, status=201)

    def get(self, request):
        games = Game.objects.filter(status="W")
        return Response(GameSerializer(games, many=True).data, status=200)


class GetGameView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, game_id):
        try:
            game = Game.objects.get(id=game_id)
            return Response(GameSerializer(game).data, status=200)
        except Game.DoesNotExist:
            return Response({"error": f"Game with ID {game_id} not found"}, status=404)


class GetAttemptView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, game_id):
        try:
            game = Game.objects.get(id=game_id)
            attempts = Attempt.objects.filter(game=game)
            return Response(AttemptSerializer(attempts, many=True).data, status=200)
        except Game.DoesNotExist:
            return Response({"error": f"Game with ID {game_id} not found"}, status=404)
