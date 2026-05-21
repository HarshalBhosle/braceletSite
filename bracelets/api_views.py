from rest_framework import viewsets
from .models import Bracelet, Category, Product
from .serializers import BraceletSerializer, CategorySerializer, ProductSerializer


class BraceletViewSet(viewsets.ModelViewSet):
    queryset = Bracelet.objects.all()
    serializer_class = BraceletSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
