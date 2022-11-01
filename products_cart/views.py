from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect

from django.contrib import messages

from django.views import View

from products.models import Product

from products_checkout.models import Order

from .models import CartProducts


class CartView(View):
    """
    Class to display the Cart
    """
    template_name = 'cart/cart.html'

    def get(self, request):

        order = Order.objects.filter(created_by=request.user, billed=False)
        cart = CartProducts.objects.filter(created_by=request.user)

        if order.exists():
            order = order[0]
        else:
            order = Order.objects.create(created_by=request.user)

        context = {
            'cart': cart,
            'order': order,
        }

        return render(request, self.template_name, context)


def AddToCart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        order = Order.objects.filter(created_by=request.user, billed=False)

        if order.exists():
            order = order[0]
            if order.cart_products.filter(created_by=request.user,
                                          product=product).exists():
                item = CartProducts.objects.get(created_by=request.user,
                                                product=product)
                item.quantity += 1
                item.save()
                messages.info(request, 'Quantity Updated!')
            else:
                item = CartProducts.objects.create(
                    created_by=request.user, product=product)
                order.cart_products.add(item)
                messages.success(request, 'Product Added to your Cart!')
        else:
            order = Order.objects.create(
                created_by=request.user)
            item = CartProducts.objects.create(
                created_by=request.user, product=product)
            order.cart_products.add(item)
            messages.success(request, 'Product Added to your Cart!')
        return HttpResponseRedirect(reverse('cart', ))


def RemoveFromCart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(CartProducts, product=product_id)
        product.delete()

        return HttpResponseRedirect(reverse('cart', ))
    

def RemoveQuantityProduct(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(CartProducts, product=product_id)
        if product.quantity > 1:
            product.quantity -= 1
            product.save()
        else:
            product.delete()
        return HttpResponseRedirect(reverse('cart', ))
    

def AddQuantityProduct(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(CartProducts, product=product_id)
        if product.quantity >= 1:
            product.quantity += 1
            product.save()
        return HttpResponseRedirect(reverse('cart', ))
