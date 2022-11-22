""" Imports """
from django.shortcuts import render
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from products.models import Product
from dashboard.models import Testimonial


class HomeView(View):
    """ View to display the homepage """
    template_name = 'home/index.html'

    def get(self, request):
        new_products = Product.objects.filter(product_status=0,
                                              is_deleted=False
                                              ).order_by('-created_at')[:4]
        used_products = Product.objects.filter(product_status=1,
                                               is_deleted=False
                                               ).order_by('-created_at')[:4]
        testimonials = Testimonial.objects.all().order_by('-created_at')[:4]

        context = {
                'new_products': new_products,
                'used_products': used_products,
                'testimonials': testimonials,
            }

        return render(request, self.template_name, context)


class LoginRequired(LoginRequiredMixin):
    """
    Extended the LoginRequiredMixin adding a Warning message
    framework to ``permission_denied_message`` attribute.
    """

    permission_denied_message = 'You have to be logged in to access that page'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 self.permission_denied_message)
            return self.handle_no_permission()
        return super(LoginRequired, self).dispatch(
            request, *args, **kwargs
        )
