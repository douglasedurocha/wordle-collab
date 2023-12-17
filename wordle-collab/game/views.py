from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


def game(request, game_id):
    return HttpResponse(f"You're looking at game {game_id}.")
