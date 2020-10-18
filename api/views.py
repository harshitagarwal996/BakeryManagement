import json

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from api.serializers import IngredientSerializer, ProductSerializer
from main import models


class RegisterBakery(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, *args, **kwargs):
        data = {key: request.data[key] for key in request.data.keys()}
        data['user'] = request.user.id
        if request.user.bakery:
            return Response("This User already has a bakery registered with us", status=status.HTTP_302_FOUND)
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
        return Response("Bakery and Inventory Created successfully, you can now add items in your Inventory", status=status.HTTP_200_OK)


class ManageInventoryIngredients(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        return Response(IngredientSerializer(request.user.bakery.inventory.ingredients, many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = {key: request.data[key] for key in request.data.keys()}
        inventory_id = self.request.user.bakery.inventory.id
        data['inventory'] = inventory_id
        ingredient = IngredientSerializer(data=data)
        ingredient.is_valid(raise_exception=True)
        ingredient.save()
        return Response("Ingredient saved successfully in your Bakery's Inventory", status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        data = {key: request.data[key] for key in request.data.keys()}
        # Check if the ingredient exists in users inventory or not
        if not data.get("id"):
            return Response("Ingredient id is required", status.HTTP_400_BAD_REQUEST)
        ingredients = request.user.bakery.inventory.ingredients
        ingredient = ingredients.filter(id=data['id']).first()
        if not ingredient:
            return Response("Requested ingredient does not exist, create one?", status=status.HTTP_200_OK)
        # Save ingredient data to database
        try:
            for (key, value) in data.items():
                setattr(ingredient, key, value)
            ingredient.save()
        except Exception as e:
            return Response(str(e), status.HTTP_400_BAD_REQUEST)
        return Response("Ingredient updated successfully in your Bakery's Inventory", status.HTTP_200_OK)


class ManageBakeryProduct(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        return Response(ProductSerializer(request.user.bakery.products, many=True).data,
                        status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if not request.data.get('ingredient_quantity_mappings'):
            return Response("Please enter the ingredient id and quantity mapping to ingredient_quantity_mappings", status.HTTP_400_BAD_REQUEST)
        data = {key: request.data[key] for key in request.data.keys()}
        bakery_id = self.request.user.bakery.id
        data['bakery'] = bakery_id
        product = ProductSerializer(data=data)
        product.is_valid(raise_exception=True)
        product = product.save()
        # TODO: optimise this
        try:
            for mapping in json.loads(request.data['ingredient_quantity_mappings']):
                mapping['product'] = product
                mapping_obj = models.IngredientQuantityMapping.objects.create(**mapping)
                mapping_obj.save()
        except Exception as e:
            return Response(str(e), status.HTTP_400_BAD_REQUEST)
        return Response("Product saved successfully in your Bakery", status.HTTP_200_OK)



# Customer APIViews starts here

class GetBakeryList(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Bakery.objects.all()
    serializer_class = serializers.BakerySerializer


class GetProductsFromBakery(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):
        if not request.GET.get('bakery_id'):
            return Response("Please enter param bakery_id", status.HTTP_400_BAD_REQUEST)
        return Response(ProductSerializer(models.Product.objects.filter(bakery=request.GET.get('bakery_id')), many=True).data,
                        status=status.HTTP_200_OK)

class CustomerOrder(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        if not request.get('bakery_id'):
            return Response("Please tell us the bakery you want to check orders from")
        return Response(ProductSerializer(request.user.bakery.products, many=True).data,
                        status=status.HTTP_200_OK)
