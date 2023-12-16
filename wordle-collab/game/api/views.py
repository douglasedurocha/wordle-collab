from game.api.serializers import AtemptSerializer
from game.models import Attempt
from rest_framework.viewsets import ModelViewSet


class AttemptViewSet(ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AtemptSerializer
