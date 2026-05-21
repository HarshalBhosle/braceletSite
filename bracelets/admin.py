from django.contrib import admin
from .models import Bracelet, Category, Product

@admin.register(Bracelet)
class BraceletAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'material', 'color', 'stock', 'created_at']
    list_filter = ['material', 'color', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'material', 'color', 'size', 'stock', 'created_at']
    list_filter = ['category', 'material', 'color', 'size']
    search_fields = ['name', 'material', 'color']
