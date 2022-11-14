import stripe
import json

from django.conf import settings

from django.core.mail import send_mail
from django.template.loader import render_to_string

from horizon_shop.settings import DEFAULT_FROM_EMAIL

from horizon_shop.settings import STRIPE_PUBLIC_KEY
from horizon_shop.settings import STRIPE_SECRET_KEY
from horizon_shop.settings import STRIPE_WH_SECRET
from horizon_shop.settings import STRIPE_CURRENCY

from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

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
        stripe_public_key = STRIPE_PUBLIC_KEY
        stripe_secret_key = STRIPE_SECRET_KEY

        order = Order.objects.get(created_by=request.user, billed=False)

        total_order = order.total_price()
        total_stripe = round(total_order * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=total_stripe,
            currency=STRIPE_CURRENCY,
            customer=stripe.Customer.create(customer=request.user),
            metadata={
                    "order_id": order.id
                }
        )

        context = {
            'order': order,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
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


@require_POST
@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = STRIPE_WH_SECRET

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            endpoint_secret
            )
    except ValueError as e:
        # Invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print(e)
        return HttpResponse(status=400)

    if event['type'] == 'charge.succeeded':
        intent = event['data']['object']

        customer_email = intent["receipt_email"]

        order_id = intent["metadata"]["order_id"]

        order = Order.objects.get(id=order_id)

        send_mail(
            subject=render_to_string(
                'text_emails/email-order-subject.txt',
                {'order': order}
                ),
            message=render_to_string(
                'text_emails/email-order-succeeded.txt',
                {'order': order, 'contact_email': DEFAULT_FROM_EMAIL}
                ),
            recipient_list=[customer_email],
            from_email=[DEFAULT_FROM_EMAIL],
            )

        order.billed = True
        order.save()

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a stripe.PaymentIntent
        print(payment_intent['receipt_email'])
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    else:
        print('Unhandled event type {}'.format(event.type))

    # Passed signature verification
    return HttpResponse(status=200)


class PaymentSuccess(View):
    template_name = 'checkout/payment-success.html'

    def get(self, request):

        context = {
            'payment_status': 'success',
        }

        return render(request, self.template_name, context)

    def post(self, request, order, *args, **kwargs):
        order = Order.objects.get(created_by=request.user, id=order)

        print("I am changing the status of the Order!!!")

        print(order)
        context = {
            'order': order,
        }
        return render(request, self.template_name, context)
