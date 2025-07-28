from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['content_type','object_id', 'quantity', 'price', 'start_date', 'end_date']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email','created_at', 'updated_at', 'status', 'total_price']
    list_filter = ['user', 'created_at', 'total_price']
    inlines = [OrderItemInline]