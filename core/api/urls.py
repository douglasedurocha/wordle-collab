from rest_framework.routers import DefaultRouter
from game.api.urls import attempt_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(attempt_router.registry)

urlpatterns = [path("", include(router.urls))]
