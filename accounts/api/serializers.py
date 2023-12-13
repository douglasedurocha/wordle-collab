from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "email", "is_superuser"]


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    def check_user(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
