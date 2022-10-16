from django.contrib import admin
from .models import Category
from .models import SubCategory
from .models import Product
from .models import ProductComments
from .models import ProductRating


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Category """
    list_display = ('name', 'friendly_name')
    list_filter = ('name', )
    search_fields = ('friendly_name', )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """ Sub-Categories """
    list_display = ('name', 'friendly_name')
    list_filter = ('name', )
    search_fields = ('friendly_name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product """
    list_display = (
        'category', 'title', 'brand',
        'release_date', 'created_by',
        'created_date', 'price', 'product_status')
    list_filter = (
        'category', 'brand', 'title', 'release_date')
    search_fields = (
        'created_by', 'category', 'created_date', 'brand', 'release_date')


@admin.register(ProductComments)
class ProductCommentsAdmin(admin.ModelAdmin):
    """ Product Comment """
    list_display = (
        'product', 'commented_by', 'commented_date', 'comment')
    list_filter = (
        'product', 'commented_by', 'commented_date')
    search_fields = (
        'product', 'commented_by', 'commented_date', 'comment')


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    """ Product Rating """
    list_display = (
        'product', 'rated_by', 'rating_stars')
    list_filter = (
        'product', 'rated_by', 'rating_stars')
    search_fields = (
        'product', 'rated_by', 'rating_stars')
