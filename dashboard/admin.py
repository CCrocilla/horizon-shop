from django.contrib import admin
from .models import Testimonial
from .models import Customer
from .models import ShippingAddress


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """ Customer """
    list_display = (
        'customer', 'customer_status', 'avatar')


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    """ Customer Shipping Address """
    list_display = (
        'created_by',
        'shipping_name',
        'country',
        'phone_number',
        'city',
        'postcode')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """ Users' Testimonials """
    list_display = (
        'created_by', 'title', 'created_date', 'rating_stars')
