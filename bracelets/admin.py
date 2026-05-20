from django.contrib import admin
from .models import Bracelet

@admin.register(Bracelet)
class BraceletAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'material', 'color', 'stock', 'created_at']
    list_filter = ['material', 'color', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
