from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """ Wishlist """
    list_display = ('user', 'product', 'created_at')
