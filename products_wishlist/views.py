from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView

from home.views import LoginRequired
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Wishlist
from products.models import Product


class WishlistView(LoginRequired, ListView):
    """
    Class to display Only Used Products
    """
    model = Wishlist
    template_name = 'dashboard/products/products-wishlist.html'
    fields = '__all__'
    permission_denied_message = 'Authentication Error! Access reserved \
                                 only to Authenticated Customers!'
    paginate_by = 8

    def get_queryset(self):
        """
        Return a list of all the Shipping Address
        for the authenticated user.
        """
        queryset = Wishlist.objects.filter(user=self.request.user)
        return queryset


def AddToWishlistView(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        redirect_url = request.POST.get('redirect_url')

        try:
            product_wished = Wishlist.objects.get(
                user=request.user, product=product)
            if product_wished:
                messages.info(
                    request,
                    f'The Product {product.title} is already in your Wishlist!'
                    )

        except Exception:
            Wishlist.objects.create(user=request.user, product=product)
            messages.success(
                request,
                f'Product {product.title} added to your Wishlist!'
                )

        finally:
            return HttpResponseRedirect(redirect_url)


def RemoveFromWishlistView(request, wished_product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=wished_product_id)
        Wishlist.objects.get(user=request.user, product=product).delete()
        messages.success(request,
                         f'Product {product.title} removed from your Wishlist!'
                         )
        return HttpResponseRedirect(reverse('products-wishlist', ))
