from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from api.serializers import TokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterBakeryAdmin(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            username = request.data["username"]
            password = request.data["password"]
            email = request.data["email"]
        except:
            return Response("username, password and email is required to register a user",
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            new_user = User.objects.create_user(username=username, password=password, email=email, is_staff=True)
        except:
            # TODO: add code for data validations
            return Response("User already exist or data validations failed", status.HTTP_409_CONFLICT)
        return Response("Bakery Admin " + username + " created successfully", status=status.HTTP_201_CREATED)


class RegisterUsersView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            username = request.data["username"]
            password = request.data["password"]
            email = request.data["email"]
        except:
            return Response("username, password and email is required to register a user",
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            new_user = User.objects.create_user(username=username, password=password, email=email, is_staff=False)
        except:
            return Response("User already exist or data validations failed", status.HTTP_409_CONFLICT)
        return Response("Customer " + username + " created successfully", status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data={"token": jwt_encode_handler(jwt_payload_handler(user))})
            serializer.is_valid()
            return Response(serializer.data)
        return Response("Please enter valid username and password", status=status.HTTP_401_UNAUTHORIZED)
