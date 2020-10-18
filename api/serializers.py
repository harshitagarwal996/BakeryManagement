from django.contrib.auth.models import User
from rest_framework import serializers

from main import models


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

class BakerySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bakery
        fields = ("__all__")

class SerializeInventory(serializers.ModelSerializer):

    class Meta:
        model = models.Inventory
        fields = ("__all__")