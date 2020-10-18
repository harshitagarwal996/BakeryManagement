from django.urls import path

from api.auth_views import RegisterBakeryAdmin, LoginView, RegisterUsersView
from api.views import RegisterBakery, ManageInventoryIngredients, ManageBakeryProduct, GetBakeryList, \
    GetProductsFromBakery

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    path('auth/register_admin/', RegisterBakeryAdmin.as_view(), name="auth-register-admin"),
    path('register_bakery/', RegisterBakery.as_view(), name="register-bakery-admin"),
    path('manage_ingredients/', ManageInventoryIngredients.as_view(), name="manage-ingredients"),
    path('manage_bakery_products/', ManageBakeryProduct.as_view(), name="manage-bakery-products"),
    path('get_bakeries/', GetBakeryList.as_view(), name="get-bakeries"),
    path('get_products_from_bakery/', GetProductsFromBakery.as_view(), name="get-bakery-products"),
]
