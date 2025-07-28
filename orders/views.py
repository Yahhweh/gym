import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.models import CartItem, Cart
from listofgyms.constants import STATUS_CHOICES
from django.contrib.contenttypes.models import ContentType
from listofgyms.models import Gym, Subscription
from people.models import CustomUser
from datetime import datetime
from people.models import Trainings
from shop.models import ShopProducts


def order_create(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.get_total_price() for item in cart_items)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.user = user
            order = form.save(commit=False)
            order.user = user
            order.status = 'paid'

            order.save()

            total_price = 0
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    content_type=item.content_type,
                    object_id=item.object_id,
                    price=item.price,
                    quantity=item.quantity,
                    start_date=item.date_start,
                    end_date=item.date_end,
                )

            for item in cart_items:
                user_content_type = ContentType.objects.get_for_model(CustomUser)
                gym_content_type = ContentType.objects.get_for_model(Gym)
                product_content_type = ContentType.objects.get_for_model(ShopProducts)
                if item.content_type == user_content_type:
                    trainer = CustomUser.objects.get(id = item.object_id)
                    trainer.profit += item.price
                    trainer.save()
                    try:
                        training = Trainings.objects.get(username=request.user, trainer= item.object_id)
                        training.quantity += item.quantity
                        training.save()
                    except Trainings.DoesNotExist:
                        training = Trainings.objects.create(
                            username=request.user,
                            trainer=item.object_id,
                            quantity=item.quantity,
                        )
                        training.save()

                elif  item.content_type == gym_content_type:
                    gym = Gym.objects.get(id = item.object_id)
                    try:
                        subscription = Subscription.objects.get(username=request.user, gym=gym)
                        subscription.quantity += item.quantity
                        subscription.save()
                        subscription.save()
                    except Subscription.DoesNotExist:
                        subscription = Subscription.objects.create(
                            username=request.user,
                            gym=gym,
                            quantity=item.quantity
                        )
                        subscription.save()
                        subscription.calculate_duration(datetime.now(), item.quantity)
                        subscription.save()

                elif item.content_type == product_content_type:
                    product = ShopProducts.objects.get(id = item.object_id)
                    order_quantity = item.quantity
                    product.quantity = product.quantity - order_quantity
                    for item in cart_items:
                        product_content_type = ContentType.objects.get_for_model(ShopProducts)
                        if item.content_type == product_content_type:
                            if product.quantity < 0:
                                return render(request, 'orders/order/error.html')
                            else:
                                product.save()

                total_price += item.get_total_price()
            order.save()
            order.total_price = total_price
            cart_items.delete()

            return render(request, 'orders/order/created.html', {'order': order})
        return None
    else:
        form = OrderCreateForm()

        return render(request, 'orders/order/create.html', {
            'cart': cart,
            'cart_items': cart_items,
            'form': form,
            'total_price': total_price
        })