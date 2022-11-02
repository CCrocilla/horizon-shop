from django.urls import path

from . import views

from .views import CheckoutView


urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    # path('', CheckoutView, name='checkout'),
]
