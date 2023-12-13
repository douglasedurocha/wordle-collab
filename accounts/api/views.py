from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer


class UserView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        SessionAuthentication,
    ]

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in"}, status=401)
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=200)


class UserRegisterView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "User created successfully"}, status=201)
        return Response(serializer.errors, status=400)


class UserLoginView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response({"message": "User logged successfully"}, status=201)
        return Response(serializer.errors, status=400)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "User logged out successfully"}, status=200)
