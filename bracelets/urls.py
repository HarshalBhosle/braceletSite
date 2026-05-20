from django.urls import path
from .views import bracelets_list, bracelet_detail

urlpatterns = [
    path('', bracelets_list, name='bracelets_list'),
    path('<int:pk>/', bracelet_detail, name='bracelet_detail'),
]
