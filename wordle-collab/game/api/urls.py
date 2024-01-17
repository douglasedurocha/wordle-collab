from django.urls import path
from . import views

urlpatterns = [
    path("", views.GameView.as_view(), name="games"),
    path("<int:game_id>", views.GetGameView.as_view(), name="get-game"),
    path("<int:game_id>/attempts", views.GetAttemptView.as_view(), name="get-attempts"),
]
