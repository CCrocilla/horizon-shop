from django.urls import path

from . import views

from .views import CheckoutView
from .views import PaymentView
# from .views import PaymentSuccess
# from .views import PaymentCancel



urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),
    # path('payment/success', CheckoutView.as_view(), name='payment-success'),
    # path('payment/cancel', CheckoutView.as_view(), name='payment-cancel'),
    # path('', CheckoutView, name='checkout'),
]
