from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
]
