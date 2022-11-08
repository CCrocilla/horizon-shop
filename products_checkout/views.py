import stripe
import json

from django.conf import settings

from horizon_shop.settings import STRIPE_PUBLIC_KEY
from horizon_shop.settings import STRIPE_SECRET_KEY
from horizon_shop.settings import STRIPE_CURRENCY

from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect

from django.contrib import messages

from django.views import View
from django.views.generic import DeleteView
from django.views.generic import DetailView

from dashboard.models import ShippingAddress
from products_cart.models import CartProducts

from .models import Order

from products_cart.forms import CheckoutForm


class CheckoutView(View):
    """
    Class to display Only Used Products
    """
    model = Order
    template_name = 'checkout/checkout.html'

    def get(self, request):
        order = Order.objects.get(created_by=request.user, billed=False)

        context = {
            'order': order,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(created_by=request.user, billed=False)

        shipping_address_id = request.POST.get('shipping_address')

        form = CheckoutForm(request.POST or None)

        if form.is_valid():
            order.created_by = request.user
            order.shipping_address = ShippingAddress.objects.get(
                created_by=request.user, id=shipping_address_id
                )
            order.total_price = request.POST.get('total_price_cart')
            order.save()

            return HttpResponseRedirect(reverse('checkout'))
        else:
            messages.error(
                request,
                'Error: Form not filled in correctly! Please try again!'
                )
            return redirect('cart')


class PaymentView(View):
    """
    Class to display Only Used Products
    """
    model = Order
    template_name = 'checkout/payment.html'

    def get(self, request):
        stripe_public_key = STRIPE_PUBLIC_KEY
        stripe_secret_key = STRIPE_SECRET_KEY

        order = Order.objects.get(created_by=request.user, billed=False)

        total_order = order.total_price()
        total_stripe = round(total_order * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=total_stripe,
            currency=STRIPE_CURRENCY
        )

        context = {
            'order': order,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, self.template_name, context)


class PaymentSuccess(View):
    template_name = 'checkout/payment-success.html'

    def get(self, request):

        context = {
            'payment_status': 'success',
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(created_by=request.user, billed=False)
        order.billed = True
        order.save()

        print("I am changing the status of the Order!!!")
        print(order.order_number)

        # context = {
        #     'order': 'order',
        # }
        
        return redirect(reverse('checkout_success', args=[order.order_number]))
        # return render(request, self.template_name, context)


# class PaymentCancel(View):
#     template_name = 'checkout/payment-cancel.html'

#     def get(self, request):

#         context = {
#             'payment_status': 'cancel',
#         }

#         return render(request, self.template_name, context)
