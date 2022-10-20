""" Imports """
from django.shortcuts import render
from django.views import View


class HomeView(View):
    """ View to display the homepage """
    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name, {})
