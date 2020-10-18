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


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ("__all__")


class IngredientQuantiyMappingSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.CharField(source="ingredient.name")

    class Meta:
        model = models.IngredientQuantityMapping
        fields = ("quantity", "ingredient_id", "ingredient_name")


class ProductSerializer(serializers.ModelSerializer):
    ingredient_quantity_mappings = IngredientQuantiyMappingSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = models.Product
        fields = ("__all__")
