from django.shortcuts import render
from django.views import View


class CartView(View):
    """
    Class to display the Cart
    """
    template_name = 'cart/cart.html'

    def get(self, request):
        return render(request, self.template_name, {})
