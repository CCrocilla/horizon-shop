from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import DashboardView

from .views import CustomerView
from .views import CustomerPasswordChangeView

from .views import TestimonialAddView
from .views import TestimonialListView
from .views import TestimonialDetailsView
from .views import TestimonialUpdateView
from .views import TestimonialDeleteView

from .views import ShippingAddressAddView
from .views import ShippingAddressListView
from .views import ShippingAddressUpdateView
from .views import ShippingAddressDeleteView

from .views import ProductAddView
from .views import ProductListView
from .views import ProductUpdateView
from .views import ProductDeleteView


urlpatterns = [
    path(
        '', DashboardView.as_view(), name='dashboard'),
    path(
        '', include('django.contrib.auth.urls')),
    ##########################################
    #            Customer Paths              #
    ##########################################
    path(
        'customer/update',
        CustomerView.as_view(),
        name='customer-update'
        ),
    path(
        'customer/change_password/',
        CustomerPasswordChangeView.as_view(),
        name='change-password'
        ),
    ##########################################
    #       Shipping Addresses Paths         #
    ##########################################
    path(
        'shpping_address/add',
        ShippingAddressAddView.as_view(),
        name='shipping-address-add'
        ),
    path(
        'shipping_address/list',
        ShippingAddressListView.as_view(),
        name='shipping-address-list'
        ),
    path(
        'shipping_address/<int:pk>/update',
        ShippingAddressUpdateView.as_view(),
        name='shipping-address-update'
        ),
    path(
        'shipping_address/<int:pk>/delete',
        ShippingAddressDeleteView.as_view(),
        name='shipping-address-delete'
        ),
    ##########################################
    #             Product Paths              #
    ##########################################
    path(
        'product/add',
        ProductAddView.as_view(),
        name='product-add'
        ),
    path(
        'product/list',
        ProductListView.as_view(),
        name='product-list'
        ),
    path(
        'product/<slug:slug>/update',
        ProductUpdateView.as_view(),
        name='product-update'
        ),
    path(
        'product/<slug:slug>/delete',
        ProductDeleteView.as_view(),
        name='product-delete'
        ),
    ##########################################
    #           Testimonial Paths            #
    ##########################################
    path(
        'testimonial/add',
        TestimonialAddView.as_view(),
        name='testimonial-add'
        ),
    path(
        'testimonial/list',
        TestimonialListView.as_view(),
        name='testimonials-list'
        ),
    path(
        'testimonial/<int:pk>/details',
        TestimonialDetailsView.as_view(),
        name='testimonial-details'
        ),
    path(
        'testimonial/<int:pk>/update',
        TestimonialUpdateView.as_view(),
        name='testimonial-update'
        ),
    path(
        'testimonial/<int:pk>/delete',
        TestimonialDeleteView.as_view(),
        name='testimonial-delete'
        ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)