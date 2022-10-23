from django.contrib import admin

from . import views

from django.urls import path
from django.urls import include

from .views import AllProductsListView
from .views import NewProductsListView
from .views import UsedProductsListView
from .views import ProductDetailsView
from .views import SearchByView


urlpatterns = [
    path('all/', AllProductsListView.as_view(), name='all_products'),
    path('new/', NewProductsListView.as_view(), name='new_products'),
    path('used/', UsedProductsListView.as_view(), name='used_products'),
    path('search_by/<slug:search_slug>/', SearchByView.as_view(), name='search_by'),
    path('<slug:slug>/details/', ProductDetailsView.as_view(), name='product_details'),
]
