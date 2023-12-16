from game.models import Attempt
from rest_framework.serializers import ModelSerializer


class AtemptSerializer(ModelSerializer):
    class Meta:
        model = Attempt
        fields = ("id", "word")
