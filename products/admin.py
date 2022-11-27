from django.contrib import admin
from .models import Category
from .models import SubCategory
from .models import Product
from .models import ProductComment
from .models import ProductRating


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Category """
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """ Sub-Categories """
    list_display = ('name', 'category')
    list_filter = ('name', 'category')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product """
    list_display = (
        'category',
        'title',
        'brand',
        'created_by',
        'created_at',
        'price',
        'discounted_price',
        'product_status')
    list_filter = (
        'category',
        'brand',
        'title')
    search_fields = (
        'created_by',
        'category',
        'created_at',
        'brand')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
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
