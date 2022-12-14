from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect

from django.core.exceptions import ObjectDoesNotExist

from django.contrib import messages

from django.views import View

from dashboard.models import ShippingAddress
from products.models import Product
from products_checkout.models import Order
from .models import CartProducts

from .forms import CheckoutForm


class CartView(View):
    """
    Class to display the Cart
    """
    model = Order
    template_name = 'cart/cart.html'

    def get(self, request):
        order = None
        cart = None
        shipping_address = None

        if request.user.is_authenticated:
            order = Order.objects.filter(
                created_by=request.user, billed=False
                )
            cart = CartProducts.objects.filter(
                created_by=request.user
                )
            shipping_address = ShippingAddress.objects.filter(
                created_by=request.user
                )

            if order.exists():
                order = order[0]
            else:
                order = Order.objects.create(created_by=request.user)

        context = {

            'form': CheckoutForm({
                'shipping_address': shipping_address, }),
            'cart': cart,
            'order': order,
            'shipping_address': shipping_address,
        }
        return render(request, self.template_name, context)


def AddToCart(request, product_id):
    """ Function to Add a Product to the User's Cart"""
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        order = Order.objects.filter(created_by=request.user, billed=False)

        if order.exists():
            order = order[0]
            product_found = None
            try:
                product_found = order.cart_products.get(
                    created_by=request.user, product=product)
                product_found.quantity += 1
                product_found.save()
                messages.info(request, 'Quantity Updated!')

            except ObjectDoesNotExist:
                product_found = CartProducts.objects.create(
                    created_by=request.user, product=product)
                order.cart_products.add(product_found)
                messages.success(request, 'Product Added to your Cart!')

        else:
            order = Order.objects.create(
                created_by=request.user)
            product_found = CartProducts.objects.create(
                created_by=request.user, product=product)
            order.cart_products.add(product_found)
            messages.success(request, 'Product Added to your Cart!')
        return HttpResponseRedirect(reverse('cart', ))


def RemoveFromCart(request, product_id):
    """ Function to Remove the Product from the Cart """
    if request.method == "POST":
        order = Order.objects.get(created_by=request.user, billed=False)

        products = CartProducts.objects.filter(
            created_by=request.user, product=product_id)

        for product in products:
            try:
                order.cart_products.remove(product)

            except Exception as e:
                print(e)

        return HttpResponseRedirect(reverse('cart', ))


def RemoveQuantityProduct(request, product_id):
    """ Function to Remove Quantity of a Product """
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)

        order = Order.objects.filter(created_by=request.user, billed=False)

        if order.exists():
            order = order[0]
            product_found = None
            try:
                product_found = order.cart_products.get(
                    created_by=request.user, product=product)
                if product_found.quantity > 1:
                    product_found.quantity -= 1
                    product_found.save()
                    messages.success(request, 'Quantity Updated!')
                else:
                    products = CartProducts.objects.filter(
                        created_by=request.user, product=product_id)
                    for product in products:
                        order.cart_products.remove(product)
            finally:
                return HttpResponseRedirect(reverse('cart', ))
        else:
            messages.error(request, 'Something went wrong! Please try again!')
            return HttpResponseRedirect(reverse('cart', ))


def AddQuantityProduct(request, product_id):
    """ Function to Add Quantity of a Product """
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)

        order = Order.objects.filter(created_by=request.user, billed=False)

        if order.exists():
            order = order[0]
            product_found = None
            try:
                product_found = order.cart_products.get(
                    created_by=request.user, product=product)
                product_found.quantity += 1
                product_found.save()

                messages.success(request, 'Quantity Updated!')

            except ObjectDoesNotExist:
                messages.error(
                    request,
                    'Something went wrong! Please try again!'
                    )
                return HttpResponseRedirect(reverse('cart', ))

                product_not_found = CartProducts.objects.create(
                    created_by=request.user, product=product)
                order.cart_products.add(product_not_found)
                messages.success(request, 'Product Added to your Cart!')
            finally:
                return HttpResponseRedirect(reverse('cart', ))
        else:
            messages.error(
                request,
                'Something went wrong! Please try again!'
                )
            return HttpResponseRedirect(reverse('cart', ))
