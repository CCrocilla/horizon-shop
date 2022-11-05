from django.contrib import admin

from django.urls import path
from django.urls import include

from .views import HomeView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
