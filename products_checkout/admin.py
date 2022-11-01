from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Order Products in Cart """
    readonly_fields = (
        'order_number',
        'created_at',
        'total_price',
        )
    list_display = (
        'order_number',
        'created_by',
        'created_at',
        'shipping_address',
        'billed',
        'delivered',
        'total_price',
        )
    list_filter = (
        'created_by',
        'created_at',
        'shipping_address',
        'billed',
        'delivered',
        )
    search_fields = (
        'created_by',
        'order_number',
        'billed',
        'delivered',
        )
