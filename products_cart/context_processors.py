from django.shortcuts import get_object_or_404

from .models import CartProducts
from products_checkout.models import Order

DELIVERY_COST = 10
FREE_DELIVERY_THRESHOLD = 60


def cart_contents(request):

    total_products_cart = 0
    total_price_cart = 0
    delivery = 0

    if request.user.is_authenticated:

        order = Order.objects.filter(created_by=request.user, billed=False)
        cart = CartProducts.objects.filter(created_by=request.user)

        if order.exists():
            order = order[0]
            total_products_cart = order.quantity_products()
            total_price_cart = order.total_price()

        if total_price_cart < FREE_DELIVERY_THRESHOLD:
            delivery = total_products_cart * DELIVERY_COST
            total_price_cart = total_price_cart + delivery

    return {
        'total_products_cart': total_products_cart,
        'total_price_cart': total_price_cart,
        'delivery_cost': delivery,
        }
