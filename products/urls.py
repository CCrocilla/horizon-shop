from django.contrib import admin

from . import views

from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from .views import AllProductsListView
from .views import NewProductsListView
from .views import UsedProductsListView
from .views import ProductDetailsView
from .views import SearchByView
from .views import SearchBySubCategoryView
from .views import ProductCommentDeleteView


urlpatterns = [
    path(
        '', include('django.contrib.auth.urls')),
    path('all/',
         AllProductsListView.as_view(),
         name='all_products'
         ),
    path('new/',
         NewProductsListView.as_view(),
         name='new_products'
         ),
    path('used/',
         UsedProductsListView.as_view(),
         name='used_products'
         ),
    path('search-by/category/<slug:search_slug>/',
         SearchByView.as_view(),
         name='search_by'
         ),
    path('search-by/subcategory/<slug:slug_sub_cat>/',
         SearchBySubCategoryView.as_view(),
         name='search_by_sub_cat'
         ),
    path('<slug:slug>/details/',
         ProductDetailsView.as_view(),
         name='product_details'
         ),
    path('comment/<int:pk>/delete',
         ProductCommentDeleteView,
         name='delete-comment'
         )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
