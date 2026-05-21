from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api_views import BraceletViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('bracelets', BraceletViewSet, basename='bracelet')
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
