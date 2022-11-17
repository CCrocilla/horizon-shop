from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.views import View

from home.views import LoginRequired
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Wishlist
from products.models import Product


class WishlistView(LoginRequired, View):
    """
    Class to display Only Used Products
    """
    model = Wishlist
    template_name = 'dashboard/products/products-wishlist.html'
    permission_denied_message = 'Restricted Access!'

    def get(self, request):
        products_wishlist = Wishlist.objects.filter(user=request.user)

        context = {
                'wishlist': products_wishlist,
            }
        return render(request, self.template_name, context)


def AddToWishlistView(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        redirect_url = request.POST.get('redirect_url')

        try:
            product_wished = Wishlist.objects.get(
                user=request.user, product=product)
            if product_wished:
                messages.error(
                    request,
                    f'The Product {product.title} is already in your Wishlist!'
                    )

        except Exception:
            Wishlist.objects.create(user=request.user, product=product)
            messages.success(
                request,
                f'Product {product.title} Added to your Wishlist!'
                )

        finally:
            return HttpResponseRedirect(redirect_url)


def RemoveFromWishlistView(request, wished_product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=wished_product_id)
        Wishlist.objects.get(user=request.user, product=product).delete()
        messages.success(request,
                         'Product Removed Successfully from your Wishlist!')
        return HttpResponseRedirect(reverse('products-wishlist', ))
