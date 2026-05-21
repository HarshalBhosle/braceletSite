from django.urls import path
from .auth_views import login_admin, logout_admin, register_admin

urlpatterns = [
    path('login/', login_admin, name='login_admin'),
    path('register/', register_admin, name='register_admin'),
    path('logout/', logout_admin, name='logout_admin'),
]
