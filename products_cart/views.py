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
    if request.method == "POST":
        order = Order.objects.get(created_by=request.user, billed=False)

        products = CartProducts.objects.filter(
            created_by=request.user, product=product_id)

        for product in products:
            try:
                order.cart_products.remove(product)
                # TO DO: The Orphan does not cancel all the Item from the Cart.
                # to_be_remove = order.cart_products.through.objects.filter(
                # cartproducts_id=product.id)
                # print("Elements to_be_remove:")
                # print(to_be_remove.all().values())

                # product_found = to_be_remove.count()
                # if product_found > 0:
                #     to_be_remove.delete()
                #     print("List of Products:")
                #     print(product)
                #     CartProducts.objects.filter(cartproducts_id=product.id).delete()
                # else:
                #     print('Product not found!')
            except Exception as e:
                print(e)

        return HttpResponseRedirect(reverse('cart', ))


def RemoveQuantityProduct(request, product_id):
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
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)

        order = Order.objects.filter(created_by=request.user, billed=False)

        if order.exists():
            order = order[0]
            product_found = None
            try:
                print("SUCCESS0")
                product_found = order.cart_products.get(
                    created_by=request.user, product=product)
                print("SUCCESS1")
                print(product_found)

                product_found.quantity += 1
                print("SUCCESS2")

                product_found.save()
                print("SUCCESS3")

                messages.success(request, 'Quantity Updated!')

            except ObjectDoesNotExist:
                print("DENIED")

                product_not_found = CartProducts.objects.create(
                    created_by=request.user, product=product)
                order.cart_products.add(product_not_found)
                messages.success(request, 'Product Added to your Cart!')
            finally:
                return HttpResponseRedirect(reverse('cart', ))
        else:
            messages.error(request, 'Something went wrong! Please try again!')
            return HttpResponseRedirect(reverse('cart', ))


# def RemoveQuantityProduct(request, product_id):
#     if request.method == "POST":
#         product = CartProducts.objects.get(
#             created_by=request.user, product=product_id)

#         if product.quantity > 1:
#             product.quantity -= 1
#             product.save()
#         else:
#             product.delete()
#         return HttpResponseRedirect(reverse('cart', ))


# def AddQuantityProduct(request, product_id):
#     if request.method == "POST":
#         product = CartProducts.objects.get(
#             created_by=request.user, product=product_id)

#         if product.quantity >= 1:
#             product.quantity += 1
#             product.save()
#         return HttpResponseRedirect(reverse('cart', ))