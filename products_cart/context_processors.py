from django.shortcuts import get_object_or_404

from .models import CartProducts
from products_checkout.models import Order

from horizon_shop.settings import DELIVERY_COST
from horizon_shop.settings import FREE_DELIVERY_THRESHOLD


def cart_contents(request):

    total_products_cart = 0
    total_price_cart = 0
    total_price_no_delivery = 0
    delivery = 0

    if request.user.is_authenticated:

        order = Order.objects.filter(created_by=request.user, billed=False)
        cart = CartProducts.objects.filter(created_by=request.user)

        if order.exists():
            order = order[0]
            total_products_cart = order.quantity_products()
            total_price_cart = order.total_price()

            for item in order.cart_products.all():
                if item.product.discounted_price:
                    total_price_no_delivery += (
                        item.product.discounted_price * item.quantity)
                else:
                    total_price_no_delivery += (
                        item.product.price * item.quantity)

    return {
        'total_products_cart': total_products_cart,
        'total_price_cart': total_price_cart,
        'delivery_cost': delivery,
        'total_price_no_delivery': total_price_no_delivery
        }
