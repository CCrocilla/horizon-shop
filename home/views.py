""" Imports """
from django.shortcuts import render
from django.views import View

from products.models import Product


class HomeView(View):
    """ View to display the homepage """
    template_name = 'home/index.html'

    def get(self, request):
        new_products = Product.objects.all()
        
        context = {
                'new_products': new_products,
            }
        
        return render(request, self.template_name, context)
