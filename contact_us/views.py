from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import ContactUs
from .forms import ContactUsForm


class ContactUsView(CreateView):
    """ Contact Page """
    template_name = 'contact_us/contact_us.html'
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('contact_us')
    success_message = "Thanks! Your request have been sent successfully!"


class TermsView(View):
    template_name = 'contact_us/terms.html'

    def get(self, request):
        return render(request, self.template_name, {})
