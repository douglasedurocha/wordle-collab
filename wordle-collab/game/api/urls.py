from django.urls import path
from . import views

urlpatterns = [
    path("list-open", views.OpenGameListView.as_view(), name="open-games"),
    path("create", views.GameCreateView.as_view(), name="create-game"),
    path("<int:game_id>", views.GetGameView.as_view(), name="get-game"),
    path("<int:game_id>/attempts", views.GetAttemptView.as_view(), name="get-attempts"),
]
