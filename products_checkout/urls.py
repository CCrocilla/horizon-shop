from django.urls import path

from . import views

from .views import CheckoutView
from .views import PaymentSuccess
from .views import PaymentFailed
from .views import stripe_webhook


urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path(
        'payment/success/<int:order_id>',
        PaymentSuccess,
        name='payment-success'
        ),
    path(
        'payment/failed/<int:order_id>',
        PaymentFailed,
        name='payment-failed'
        ),
]
