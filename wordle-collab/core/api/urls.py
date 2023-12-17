from django.urls import path, include

urlpatterns = [
    path("", include("game.api.urls")),
    path("accounts/", include("accounts.api.urls")),
]
