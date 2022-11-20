from . import views
from django.urls import path
from django.urls import include
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
from .views import ProductsDeletedListView
from .views import ProductDeleteView
from .views import ProductRestoreView

from .views import OrderListView
from .views import OrderDetailsView

from .views import CategoryAddView
from .views import CategoryListView
from .views import CategoryUpdateView
from .views import CategoryDeleteView
from .views import CategoryRestoreView
from .views import CategoriesDeletedListView

from .views import SubCategoryAddView
from .views import SubCategoryListView
from .views import SubCategoryUpdateView
from .views import SubCategoryDeleteView
from .views import SubCategoryRestoreView
from .views import SubCategoriesDeletedListView

from products_wishlist.views import WishlistView
from products_wishlist.views import AddToWishlistView
from products_wishlist.views import RemoveFromWishlistView


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
        'shipping-address/add',
        ShippingAddressAddView.as_view(),
        name='shipping-address-add'
        ),
    path(
        'shipping-address/list',
        ShippingAddressListView.as_view(),
        name='shipping-address-list'
        ),
    path(
        'shipping-address/<int:pk>/update',
        ShippingAddressUpdateView.as_view(),
        name='shipping-address-update'
        ),
    path(
        'shipping-address/<int:pk>/delete',
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
        'products/list',
        ProductListView.as_view(),
        name='products-list'
        ),
    path(
        'product/<slug:slug>/update',
        ProductUpdateView.as_view(),
        name='product-update'
        ),
    path(
        'products/deleted/list',
        ProductsDeletedListView.as_view(),
        name='products-deleted-list'
        ),
    path(
        'product/<slug:slug>/delete',
        views.ProductDeleteView,
        name='product-delete'
        ),
    path(
        'product/<slug:slug>/restore',
        views.ProductRestoreView,
        name='product-restore'
        ),
    ##########################################
    #              Orders Paths              #
    ##########################################
    path(
        'order/list',
        OrderListView.as_view(),
        name='order-list'
        ),
    path(
        'order/<int:pk>/',
        OrderDetailsView.as_view(),
        name='order-details'
        ),
    ##########################################
    #             Wishlist Paths             #
    ##########################################
    path(
        'wishlist/',
        WishlistView.as_view(),
        name='products-wishlist'
        ),
    path(
        'wishlist/<int:product_id>',
        AddToWishlistView,
        name='add-to-wishlist'
        ),
    path(
        'remove-from-wishlist/<int:wished_product_id>',
        RemoveFromWishlistView,
        name='remove-from-wishlist'
        ),
    ##########################################
    #             Category Paths             #
    ##########################################
    path(
        'category/add',
        CategoryAddView.as_view(),
        name='category-add'
        ),
    path(
        'category/list',
        CategoryListView.as_view(),
        name='category-list'
        ),
    path(
        'category/<int:pk>/update',
        CategoryUpdateView.as_view(),
        name='category-update'
        ),
    path(
        'category/<int:pk>/delete',
        CategoryDeleteView,
        name='category-delete'
        ),
    path(
        'category/<int:pk>/restore',
        views.CategoryRestoreView,
        name='category-restore'
        ),
    path(
        'deleted/category/list',
        CategoriesDeletedListView.as_view(),
        name='deleted-category-list'
        ),
    ##########################################
    #           Sub-Category Paths           #
    ##########################################
    path(
        'sub-category/add',
        SubCategoryAddView.as_view(),
        name='subcategory-add'
        ),
    path(
        'sub-category/list',
        SubCategoryListView.as_view(),
        name='subcategory-list'
        ),
    path(
        'sub-category/<int:pk>/update',
        SubCategoryUpdateView.as_view(),
        name='subcategory-update'
        ),
    path(
        'sub-category/<int:pk>/delete',
        SubCategoryDeleteView,
        name='subcategory-delete'
        ),
    path(
        'sub-category/<int:pk>/restore',
        views.SubCategoryRestoreView,
        name='subcategory-restore'
        ),
    path(
        'deleted/sub-category/list',
        SubCategoriesDeletedListView.as_view(),
        name='deleted-subcategory-list'
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
