from django.contrib import admin
from .models import CartProducts
from .models import Order


@admin.register(CartProducts)
class CartProductsAdmin(admin.ModelAdmin):
    """ Product Cart """
    list_display = ('created_by', 'product', 'quantity')
    list_filter = ('created_by', )
    search_fields = ('created_by', 'product')


@admin.register(Order)
class OrderCartAdmin(admin.ModelAdmin):
    """ Order Products in Cart """
    list_display = ('created_by', 'created_at', 'shipping_address',
                    'billed',  'delivered',  'total_price',)
    list_filter = ('created_by', 'created_at', 'shipping_address',
                   'billed',  'delivered',)
    search_fields = ('created_by', 'order_cart_number', 'billed',
                     'delivered',)
