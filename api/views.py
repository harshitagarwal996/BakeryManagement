from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, status, generics

from api.serializers import TokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data={
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response("Please enter valid username and password", status=status.HTTP_401_UNAUTHORIZED)



class RegisterUsersView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)


class ListSongsView(ListAPIView):
    """
    Provides a get method handler.
    """
    # queryset = Songs.objects.all()
    # serializer_class = SongsSerializer
    # permission_classes = (permissions.IsAuthenticated,)