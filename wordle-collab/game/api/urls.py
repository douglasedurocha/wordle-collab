from django.urls import path
from . import views

urlpatterns = [
    path("open", views.OpenGameListView.as_view(), name="open-games"),
    path("create", views.GameCreateView.as_view(), name="create-game"),
]
