from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class DashboardView(View):
    """ Dashboard User """
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        return render(request, self.template_name, {})