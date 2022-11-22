from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import ContactUs
from .forms import ContactUsForm


class ContactUsView(SuccessMessageMixin, CreateView):
    """ Contact Page """
    template_name = 'contact_us/contact-us.html'
    model = ContactUs
    form_class = ContactUsForm
    success_message = "Thanks! Your request have been sent successfully!"
    success_url = reverse_lazy('contact_us')

    def get_initial(self):
        return {'created_by': self.request.user}


class TermsView(View):
    template_name = 'contact_us/terms.html'

    def get(self, request):
        return render(request, self.template_name, {})
