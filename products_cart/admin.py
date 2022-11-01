from django.contrib import admin
from .models import CartProducts

from products.models import Product


@admin.register(CartProducts)
class CartProductsAdmin(admin.ModelAdmin):
    """ Product Cart """
    list_display = (
        'created_by',
        'product',
        'quantity'
        )
    list_filter = (
        'created_by',
        )
    search_fields = (
        'created_by',
        'product'
        )
