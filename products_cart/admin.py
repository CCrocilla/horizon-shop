from django.contrib import admin
from .models import Category
from .models import SubCategory



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
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product """
    list_display = (
        'category', 'title', 'brand',
        'created_by', 'created_at',
        'price', 'product_status')
    list_filter = (
        'category', 'brand', 'title')
    search_fields = (
        'created_by', 'category', 'created_at', 'brand')
    prepopulated_fields = {'slug': ('title',)}