from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import  cart
from listofgyms.models import Gym
from shop.models import ShopProducts

from .models import CartItem, Cart
from people.models import CustomUser
from listofgyms.constants import PRODUCT_CHOICES


def cart_add(request, id, model_type):
    if request.method == 'POST':
        if model_type == 'gym':
            product = get_object_or_404(Gym, id = id)
        elif model_type == 'trainer':
            product = get_object_or_404(CustomUser, id=id)
        elif model_type == 'product':
            product = get_object_or_404(ShopProducts, id=id)
        else:
            raise ValueError("Invalid model_type")
        cart_item = cart.add_to_cart(request.user, product)
    else:
        pass
    return redirect('cart:cart_view')

def cart_change(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, id= id)
        cart_item.quantity += quantity
        cart_item.save()
    else:
        pass
    return redirect('cart:cart_view')


def cart_view(request):
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)

    cart_items = CartItem.objects.filter(cart=cart)

    total_items = sum(item.quantity for item in cart_items)
    total_price = sum(item.quantity * item.price for item in cart_items)

    return render(request, 'cart/cart_list.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total_items': total_items,
        'total_price': total_price,
        'user': user
    })


def cart_del(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.quantity -= 1
    if cart_item.quantity < 1:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('cart:cart_view')
