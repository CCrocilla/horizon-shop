from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.forms import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Testimonial
from .form import TestimonialForm
from .models import ShippingAddress
from .form import ShippingAddressForm


class DashboardView(View):
    """ Dashboard User """
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        return render(request, self.template_name, {})


################################
#        Customer Views        #
################################




################################
#    Shipping Address Views    #
################################
class ShippingAddressAddView(SuccessMessageMixin, CreateView):
    """
    Class to create Users' Shipping Addresses
    """
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'dashboard/customer/shipping-address-add.html'
    success_url = reverse_lazy('shipping-address-list')
    success_message = 'Shipping Address was created successfully!'

    def get_initial(self):
        user = self.request.user
        return {'created_by': user}


class ShippingAddressListView(ListView):
    """
    Class to display the User's Shipping Addresses
    """
    model = ShippingAddress
    template_name = 'dashboard/customer/shipping-address-list.html'
    ordering = ['-created_date']
    fields = '__all__'

    def get_shipping_address_auth_user(self):
        """
        Return a list of all the Shipping Address
        for the authenticated user.
        """
        user = self.request.user
        return ShippingAddress.objects.filter(created_by=user)


class ShippingAddressUpdateView(UpdateView):
    """
    Class to update User's Testimonial
    """
    model = ShippingAddress
    template_name = 'dashboard/customer/shipping-address-update.html'
    fields = '__all__'
    success_url = reverse_lazy('shipping-address-list')
    success_message = "Shipping Address updated successfully!"


class ShippingAddressDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Testimonial
    """
    model = ShippingAddress
    template_name = 'dashboard/customer/shipping-address-delete.html'
    success_url = reverse_lazy('shipping-address-list')
    success_message = "Shipping Address deleted successfully!"


################################
#       Testimonial Views      #
################################
class TestimonialAddView(SuccessMessageMixin, CreateView):
    """
    Class to create Users' Testimonial
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'dashboard/testimonials/testimonial-add.html'
    success_url = reverse_lazy('shipping-address-list')
    success_message = "Testimonial was created successfully!"

    def get_initial(self):
        user = self.request.user
        return {'created_by': user}


class TestimonialListView(ListView):
    """
    Class to display the User's Testimonial
    """
    model = Testimonial
    template_name = 'dashboard/testimonials/testimonials-list.html'
    ordering = ['-created_date']
    fields = '__all__'

    def get_testimonial_auth_user(self):
        """
        Return a list of all the Testimonial
        for the authenticated user.
        """
        user = self.request.user
        return Testimonial.objects.filter(created_by=user)


class TestimonialDetailsView(DetailView):
    """
    Class to display single User's Testimonial
    """
    model = Testimonial
    queryset = Testimonial.objects.order_by('-created_date')
    template_name = 'dashboard/testimonials/testimonial-details.html'
    fields = '__all__'


class TestimonialUpdateView(UpdateView):
    """
    Class to update User's Testimonial
    """
    model = Testimonial
    template_name = 'dashboard/testimonials/testimonial-update.html'
    fields = ['title', 'comment']
    success_url = reverse_lazy('shipping-address-list')
    success_message = "Testimonial updated successfully!"


class TestimonialDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Testimonial
    """
    model = Testimonial
    template_name = 'dashboard/testimonials/testimonial-delete.html'
    success_url = reverse_lazy('testimonials-list')
    success_message = "Testimonial deleted successfully!"
