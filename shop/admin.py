from django.contrib import admin
from .models import ShopProducts, Category


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    fields = ['title', 'slug']
    prepopulated_fields = {'slug':('title',)}

@admin.register(ShopProducts)
class AdminShopProducts(admin.ModelAdmin):
    fields =  ['title','slug', 'description','category', 'image', 'price', 'quantity']
    list_display = ['title', 'slug', 'description', 'image', 'price', 'quantity']
    prepopulated_fields = {'slug':('title',)}

