from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import User


from .models import Testimonial
from .form import TestimonialForm


class DashboardView(View):
    """ Dashboard User """
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        return render(request, self.template_name, {})
    
    
################################
#        Testimonial Views        #
################################
class TestimonialAddView(SuccessMessageMixin, CreateView):
    """
    Class to create Users' Testimonial
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'dashboard/testimonials/testimonial-add.html'
    success_url = reverse_lazy('testimonial-list')
    success_message = "Testimonial was created successfully!"

    def get_initial(self):
        return {'created_by': self.request.user}


class TestimonialListView(ListView):
    """
    Class to display the User's Testimonial
    """
    model = Testimonial
    template_name = 'dashboard/testimonials/testimonial-list.html'
    ordering = ['-created_date']
    fields = '__all__'

    def get_testimonial_auth_user(self):
        """
        This should return a list of all the Testimonial
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


class TestimonialDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Testimonial
    """
    model = Testimonial
    template_name = 'dashboard/testimonials/testimonial-delete.html'
    success_url = reverse_lazy('testimonial-list')
    success_message = "Testimonial deleted successfully!"
