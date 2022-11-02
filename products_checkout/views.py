from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect

from django.contrib import messages

from django.views import View
from django.views.generic import DeleteView
from django.views.generic import DetailView

from dashboard.models import ShippingAddress
from products_cart.models import CartProducts
from .models import Order

from .forms import CheckoutForm


class CheckoutView(View):
    """
    Class to display Only Used Products
    """
    model = Order
    template_name = 'checkout/checkout.html'

    def get(self, request):
        order = Order.objects.get(created_by=request.user, billed=False)

        context = {
            'order': order,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(created_by=request.user, billed=False)

        shipping_address_id = request.POST.get('shipping_address')

        form = CheckoutForm(request.POST or None)

        if form.is_valid():

            order.created_by = request.user
            order.shipping_address = ShippingAddress.objects.get(
                created_by=request.user, id=shipping_address_id
                )
            order.total_price = request.POST.get('total_price_cart')
            order.delivery_cost = request.POST.get('delivery_cost')
            order.save()

            return HttpResponseRedirect(reverse('checkout'))
        else:
            messages.info(
                request,
                'Error: Form not filled in correctly! Please try again!'
                )
            return redirect(request.path)
