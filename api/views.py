from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from api import serializers




class RegisterBakery(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, *args, **kwargs):
        data = {key: request.data[key] for key in request.data.keys()}
        data['user'] = request.user.id
        serialized_data = serializers.BakerySerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        bakery = serialized_data.save()
        inventory_data = serializers.SerializeInventory(
            data = {
                "name": data["bakery_name"]+" Inventory",
                "bakery": bakery.id
            }
        )
        inventory_data.is_valid()
        inventory_data.save()
        return Response("Success", status=status.HTTP_200_OK)



class ListSongsView(ListAPIView):
    """
    Provides a get method handler.
    """
    # queryset = Songs.objects.all()
    # serializer_class = SongsSerializer
    # permission_classes = (permissions.IsAuthenticated,)
