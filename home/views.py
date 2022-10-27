""" Imports """
from django.shortcuts import render
from django.views import View

from products.models import Product
from dashboard.models import Testimonial


class HomeView(View):
    """ View to display the homepage """
    template_name = 'home/index.html'

    def get(self, request):
        new_products = Product.objects.filter(product_status=0
                                              ).order_by('-created_date')[:3]
        used_products = Product.objects.filter(product_status=1
                                               ).order_by('-created_date')[:3]
        testimonials = Testimonial.objects.all().order_by('-created_date')[:3]

        context = {
                'new_products': new_products,
                'used_products': used_products,
                'testimonials': testimonials,
            }

        return render(request, self.template_name, context)
