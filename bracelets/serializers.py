from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'created_at',
            'updated_at',
        ]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'category_name',
            'name',
            'description',
            'price',
            'material',
            'color',
            'size',
            'stock',
            'image',
            'image_url',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
            'image_url': {'required': False, 'allow_blank': True},
        }
