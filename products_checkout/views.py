from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect

from django.contrib import messages

from django.views import View

from products_cart.models import CartProducts
from dashboard.models import ShippingAddress

from .models import Order

from .forms import CheckoutForm


class CheckoutView(View):
    """
    Class to display Only Used Products
    """
    model = Order
    template_name = 'checkout/checkout.html'

    def get(self, request):
        checkout_form = CheckoutForm(request.POST)

        order = Order.objects.get(created_by=request.user, billed=False)
        cart = CartProducts.objects.filter(created_by=request.user)
        shipping_address = ShippingAddress.objects.filter(created_by=request.user)

        context = {
            'form': checkout_form,
            'order': order,
            'cart': cart,
            'shipping_address': shipping_address,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        checkout_form = CheckoutForm(request.POST)

        if checkout_form.is_valid():

            checkout_form.save()
            print("Hello World!!!")
            messages.success(request, "Information Saved!")
            return HttpResponseRedirect(reverse('checkout'))


def GoToCheckout(request, *args, **kwargs):
    if request.method == 'POST':
        order = Order.objects.get(created_by=request.user, billed=False)

        if order.cart_products.filter(created_by=request.user).exists():
            order.created_by = request.user
            order.shipping_address = request.POST.get('shippping_address')
            order.total_price = request.POST.get('total_price_cart')
            order.delivery_cost = request.POST.get('delivery_cost')
            print(order.shipping_address)
            print(order.total_price)
            print(order.delivery_cost)
            order.save()

            messages.success(request, "Information Saved!")
            return HttpResponseRedirect(reverse('checkout-view'))
        else:
            messages.error(request, "There are no products in your cart!")
            return HttpResponseRedirect(reverse('checkout-view'))