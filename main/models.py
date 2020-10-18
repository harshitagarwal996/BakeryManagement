from datetime import datetime

from django.contrib.auth.models import User
from django.core import validators
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.db.models import Model


class Bakery(Model):
    user = models.OneToOneField(User, verbose_name="Bakery Owner", null=False, blank=False, on_delete=models.CASCADE)
    bakery_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    gst_number = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True, validators=[validators.MinLengthValidator(10), validators.DecimalValidator(max_digits=10, decimal_places=0)])

class Inventory(Model):
    name = models.CharField(max_length=50)
    # one inventory for each bakery
    bakery = models.OneToOneField(Bakery, related_name="inventory", on_delete=models.CASCADE)

class Ingredient(Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price_per_unit = models.IntegerField(null=False, blank=False)
    measurement_unit = models.CharField(max_length=10, null=False, blank=False)
    quantity_available = models.IntegerField()
    inventory = models.ForeignKey(Inventory, null=False, blank=False, related_name="ingredients", on_delete=models.CASCADE)


class Product(Model):
    price = models.IntegerField(null=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    bakery = models.ForeignKey(Bakery, related_name="products", null=False, blank=False, on_delete=models.CASCADE)


class IngredientQuantityMapping(Model):
    # Maps the quantity required for particular ingredient used in linked product
    product = models.ForeignKey(Product, related_name="ingredient_quantity_mappings", null=False, blank=False, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)


class SalesOrder(Model):
    invoice_number  = models.CharField(max_length=200)
    gst_number = models.CharField(max_length=50)
    customer = models.ForeignKey(User, related_name="purchase_history", on_delete=models.DO_NOTHING)
    total_amount = models.IntegerField()
    bakery = models.ForeignKey(Bakery, null=False, blank=False, related_name="sales_orders", on_delete=models.CASCADE)
    date_of_purchase = models.DateTimeField(default=datetime.now())


class SalesOrderLine(Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=False)
    sales_order = models.ForeignKey(SalesOrder, null=False, blank=False, on_delete=models.CASCADE)


class Customer(Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)