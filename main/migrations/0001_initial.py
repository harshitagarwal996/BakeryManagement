# Generated by Django 3.1.2 on 2020-10-18 05:52

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bakery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bakery_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('gst_number', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.DecimalValidator(decimal_places=0, max_digits=10)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Bakery Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price_per_unit', models.IntegerField()),
                ('measurement_unit', models.CharField(max_length=10)),
                ('quantity_available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('bakery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.bakery')),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=200)),
                ('gst_number', models.CharField(max_length=50)),
                ('total_amount', models.IntegerField()),
                ('date_of_purchase', models.DateTimeField(default=datetime.datetime(2020, 10, 18, 5, 52, 43, 922480))),
                ('bakery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_orders', to='main.bakery')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchase_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.product')),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.salesorder')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bakery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='main.bakery')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientQuantityMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ingredient')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_quantity_mappings', to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='main.inventory'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
