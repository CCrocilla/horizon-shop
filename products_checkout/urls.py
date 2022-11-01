from django.urls import path

from . import views

from .views import CheckoutView
from .views import GoToCheckout


urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout-view'),
    path(
        'checkout/',
        GoToCheckout,
        name='checkout'
        ),
]
