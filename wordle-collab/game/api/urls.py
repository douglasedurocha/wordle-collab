from rest_framework.routers import DefaultRouter
from .views import AttemptViewSet

attempt_router = DefaultRouter()
attempt_router.register(r"attempts", AttemptViewSet)
