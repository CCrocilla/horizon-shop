from django.urls import path
from .views import ContactUsView
from .views import TermsView


urlpatterns = [
    path('', ContactUsView.as_view(), name='contact_us'),
    path('terms/', TermsView.as_view(), name='terms'),
]