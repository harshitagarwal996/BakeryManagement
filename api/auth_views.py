from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response


class RegisterBakeryAdmin(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            username = request.data["username"]
            password = request.data["password"]
            email = request.data["email"]
        except:
            return Response("message": "username, password and email is required to register a user", status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email, is_staff=True
        )
        return Response("Bakery Admin "+ username + " created successfully", status=status.HTTP_201_CREATED)

