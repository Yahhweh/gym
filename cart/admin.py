from django.contrib import admin
from . import  models

@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'content_type', 'object_id', 'product', 'price', 'quantity', 'date_start', 'date_end']

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_created']