import stripe
import datetime
import json

from django.utils import timezone

from django.conf import settings

from django.core.mail import send_mail
from django.template.loader import render_to_string
from smtplib import SMTPException

from horizon_shop.settings import DEFAULT_FROM_EMAIL

from horizon_shop.settings import STRIPE_PUBLIC_KEY
from horizon_shop.settings import STRIPE_SECRET_KEY
from horizon_shop.settings import STRIPE_WH_SECRET
from horizon_shop.settings import STRIPE_CURRENCY

from horizon_shop.settings import DELIVERY_COST
from horizon_shop.settings import FREE_DELIVERY_THRESHOLD

from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from home.views import LoginRequired

from django.contrib import messages

from django.views import View
from django.views.generic import DeleteView
from django.views.generic import DetailView

from .models import Order

from dashboard.models import ShippingAddress
from products_cart.models import CartProducts

from products_cart.forms import CheckoutForm

# from products_cart.context_processors import DELIVERY_COST
# from products_cart.context_processors import FREE_DELIVERY_THRESHOLD


class CheckoutView(LoginRequired, View):
    """
    Class to display Only Used Products
    """
    model = Order
    template_name = 'checkout/checkout.html'
    permission_denied_message = 'Authentication Error! Access reserved \
                                 only to Authenticated Customers!'

    def get(self, request):
        stripe_public_key = STRIPE_PUBLIC_KEY
        stripe_secret_key = STRIPE_SECRET_KEY

        order = Order.objects.get(created_by=request.user, billed=False)

        if order.shipping_address:
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
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'No Shipping Address detected! Please select an address!'
                )
            return redirect(reverse('cart'))

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(created_by=request.user, billed=False)

        shipping_address_id = request.POST.get('shipping_address')

        form = CheckoutForm(request.POST or None)

        if form.is_valid():
            order.created_by = request.user
            order.shipping_address = ShippingAddress.objects.get(
                created_by=request.user, id=shipping_address_id
                )
            order.total_price = order.total_price()
            if order.total_price < FREE_DELIVERY_THRESHOLD:
                order.total_price += DELIVERY_COST
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

        customer_email = intent['receipt_email']
        amount = intent['amount']

        order_id = intent["metadata"]["order_id"]
        order = Order.objects.get(id=order_id)
        order.total_price = amount / 100
        order.save()

        try:
            send_mail(
                subject=render_to_string(
                    'text_emails/email-order-subject.txt',
                    {'order': order}
                    ),
                message=render_to_string(
                    'text_emails/email-order-succeeded.txt',
                    {'order': order, 'contact_email': DEFAULT_FROM_EMAIL}
                    ),
                recipient_list=[customer_email, ],
                from_email=DEFAULT_FROM_EMAIL,
            )
        except SMTPException as e:
            print('There was an error sending an email: ', e)

        PaymentSuccess(request, order_id, )

    elif event['type'] == 'charge.failed':
        intent = event['data']['object']
        order_id = intent["metadata"]["order_id"]

        PaymentFailed(request, order_id)

    else:
        print('Unhandled event type {}'.format(event.type))

    # Passed signature verification
    return HttpResponse(status=200, )


def PaymentSuccess(request, order_id,):
    """
    Payment Success
    """
    order = get_object_or_404(Order, id=order_id)
    order.created_at = datetime.datetime.now(tz=timezone.utc)
    order.billed = True
    order.save()

    messages.success(request, f'Order successfully processed! \
        Order number: {order.order_number}. A confirmation \
        email will be sent to { order.created_by.email }.')

    template_name = 'checkout/payment-success.html'
    context = {
        'order': order,
    }

    return render(request, template_name, context)


def PaymentFailed(request, order_id):
    """
    Payment Failed
    """
    order = get_object_or_404(Order, id=order_id)
    order.billed = False
    order.save()

    messages.error(request, f'There has been an issue with your \
        order. Please contact the support for further details.')

    template_name = 'checkout/payment-failed.html'
    context = {
        'order': order,
    }

    return render(request, template_name, context)
