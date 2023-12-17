from django.urls import path
from . import consumers

websocket_urlpatterns = [path(r"ws/<game_id>", consumers.GameConsumer.as_asgi())]
