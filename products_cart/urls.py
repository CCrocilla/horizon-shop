from django.urls import path

from . import views
from .views import CartView
from .views import AddToCart
from .views import RemoveFromCart
from .views import RemoveQuantityProduct
from .views import AddQuantityProduct


urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path(
        'add-to-cart/<int:product_id>',
        AddToCart,
        name='add-to-cart'
        ),
    path(
        'remove-from-cart/<int:product_id>',
        RemoveFromCart,
        name='remove-from-cart'
        ),
    path(
        'remove-quantity/<int:product_id>',
        RemoveQuantityProduct,
        name='remove-quantity'
        ),
    path(
        'add-quantity/<int:product_id>',
        AddQuantityProduct,
        name='add-quantity'
        ),
]
