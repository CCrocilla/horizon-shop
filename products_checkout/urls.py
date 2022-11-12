from django.urls import path

from . import views

from .views import CheckoutView
# from .views import PaymentView
from .views import PaymentSuccess
# from .webhooks import webhook
from .views import stripe_webhook


urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    # path('payment/', PaymentView.as_view(), name='payment'),
    path(
        'payment/success/<int:order>',
        PaymentSuccess.as_view(),
        name='payment-success'
        ),
    
    # path('payment/wh/', webhook, name='webhook')
    # path('payment/cancel', CheckoutView.as_view(), name='payment-cancel'),
    # path('', CheckoutView, name='checkout'),
]
