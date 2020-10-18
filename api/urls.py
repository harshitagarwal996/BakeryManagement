from django.urls import path

from api.auth_views import RegisterBakeryAdmin, LoginView, RegisterUsersView
from api.views import RegisterBakery

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    path('auth/register_admin/', RegisterBakeryAdmin.as_view(), name="auth-register-admin"),
    path('register_bakery/', RegisterBakery.as_view(), name="register-bakery-admin"),
]
