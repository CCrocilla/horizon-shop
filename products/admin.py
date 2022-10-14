from django.contrib import admin
from .models import Category
from .models import SubCategory
from .models import Product


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
class BookingAdmin(admin.ModelAdmin):
    """ Booking """
    list_display = (
        'category', 'title', 'brand',
        'release_date', 'created_by',
        'created_date', 'price', 'product_status')
    list_filter = (
        'category', 'brand', 'title', 'release_date')
    search_fields = (
        'created_by', 'category', 'created_date', 'brand', 'release_date')
