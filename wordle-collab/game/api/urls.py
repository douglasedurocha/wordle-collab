from django.urls import path
from . import views

urlpatterns = [
    path("create", views.GameCreateView.as_view(), name="create-game"),
]
