from django.contrib import admin
from .models import ProductCart
from .models import OrderCart


@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    """ Product Cart """
    list_display = ('created_by', 'product', 'quantity')
    list_filter = ('created_by', )
    search_fields = ('created_by', 'product')


@admin.register(OrderCart)
class OrderCartAdmin(admin.ModelAdmin):
    """ Order Cart """
    list_display = ('created_by', 'created_at', 'shipping_address',
                    'billed',  'delivered',  'total_price',)
    list_filter = ('created_by', 'created_at', 'shipping_address',
                   'billed',  'delivered',)
    search_fields = ('created_by', 'order_cart_number', 'billed',
                     'delivered',)
