from django.views.generic import ListView, TemplateView, View, DetailView
from django.shortcuts import render
from unicodedata import category

from .models import ShopProducts, Category

class ListProducts(ListView):
    template_name = 'shop/list_of_products.html'
    model = ShopProducts
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ListProductsByCategory(ListView):
    template_name = 'shop/list_of_products_by_category.html'
    model = ShopProducts
    context_object_name = 'products_by_category'

    def get_queryset(self):
        category_title = self.kwargs.get('title')
        return ShopProducts.objects.filter(category__title=category_title)


class ProductDetail(DetailView):
        template_name = 'shop/product_detail.html'
        model = ShopProducts
        context_object_name = 'product'