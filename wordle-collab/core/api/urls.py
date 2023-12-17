from django.urls import path, include

urlpatterns = [
    path("games/", include("game.api.urls")),
    path("accounts/", include("accounts.api.urls")),
]
