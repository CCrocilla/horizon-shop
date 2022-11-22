"""horizon_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

from .views import ErrorPage404

from django.contrib.sitemaps.views import sitemap

from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('contact-us/', include('contact_us.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('products_cart.urls')),
    path('checkout/', include('products_checkout.urls')),
    path('dashboard/', include('dashboard.urls')),
    # Added Robot.txt and Sitemap.xml to the views as studied on ordinarycoders
    # https://ordinarycoders.com/blog/article/robots-text-file-django
    path(
        "sitemap.xml",
        TemplateView.as_view(
            template_name="home/sitemap.xml", content_type="text/xml"
        ),
    ),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="home/robots.txt", content_type="text/plain"
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'horizon_shop.views.ErrorPage404'
