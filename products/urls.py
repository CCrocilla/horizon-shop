from django.contrib import admin
from . import views
from django.urls import path
from django.urls import include
from .views import NewProductsListView
from .views import UsedProductsListView
from .views import ProductDetailsView
from .views import get_all_new_products


urlpatterns = [
#     path('new/',
#          NewProductsListView.as_view(), name='new_products'),
    path('new/',
         views.get_all_new_products, name='new_products'),
    path('used/',
         UsedProductsListView.as_view(), name='used_products'),
    path('product/<int:pk>/details',
         ProductDetailsView.as_view(), name='product_details'),
]
