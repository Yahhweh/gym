from django.contrib.contenttypes.models import ContentType
from .models import Cart, CartItem


def add_to_cart(user, product, quantity=1):
    cart, created = Cart.objects.get_or_create(user=user)

    content_type = ContentType.objects.get_for_model(product)

    try:
        item = CartItem.objects.get(
            cart=cart,
            content_type=content_type,
            object_id=product.id
        )
        item.quantity += quantity
        item.save()
    except CartItem.DoesNotExist:
        item = CartItem.objects.create(
            cart=cart,
            content_type=content_type,
            object_id=product.id,
            quantity=quantity,
            price=product.price
        )

    return item




