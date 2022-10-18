from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import User
from .models import Product
from .models import Category
from .models import SubCategory


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def subcategories(request):
    return {
        'subcategories': SubCategory.objects.all()
    }


class NewProductsListView(ListView):
    """
    Class to display the List of New Product
    """
    model = Product
    queryset = Product.objects.filter(product_status=0).order_by('-created_date')
    queryset = Product.objects.all()
    template_name = 'products/new_products.html'
    fields = '__all__'


class UsedProductsListView(ListView):
    """
    Class to display the List of Used Product
    """
    model = Product
    # queryset = Product.objects.filter(
    #     product_status=1).order_by('-created_date')
    queryset = Product.objects.all()
    template_name = 'products/used_products.html'
    paginate_by = 6


def get_all_new_products(request):
    products = Product.objects.all()
    return render(request, 'products/new_products.html', {'products': products})


class ProductDetailsView(DetailView):
    """
    Class to display single Product
    """
    model = Product
    queryset = Product.objects.order_by('-created_date')
    template_name = 'products/product_details.html'
    fields = '__all__'
