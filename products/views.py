from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import User
from .models import Product
from .models import Category
from .models import SubCategory
from django.db.models import Q


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def subcategories(request):
    return {
        'subcategories': SubCategory.objects.all()
    }


class AllProductsListView(View):
    """
    Class to display Users' Dashboard
    """
    model = Product()
    template_name = 'products/all_products.html'

    def get(self, request):
        products = Product.objects.order_by('-created_date')
        search_term = None

        if 'q' in request.GET:
            search_term = request.GET['q']
            if not search_term:
                messages.error(request, messages.ERROR, 'No Search createria entered!')
                return redirect(reverse('all_products'))

            searched = Q(title__icontains=search_term) | Q(description__icontains=search_term) | Q(brand__icontains=search_term)
            products = products.filter(searched).order_by('-created_date')
            print(products)
            
        context = {
                'products': products,
                'search_term': search_term
            }
        return render(request, self.template_name, context)


class SearchByView(View):
    model = Product()
    template_name = 'products/search_by.html'

    def get(self, request, search_slug):
        category = get_object_or_404(Category, slug=search_slug)
        products = Product.objects.filter(category=category)

        context = {
                'products': products,
                'category': category,
            }

        return render(request, self.template_name, context)


class NewProductsListView(View):
    """
    Class to display Only New Products
    """
    model = Product()
    template_name = 'products/new_products.html'
    paginate_by = 6

    def get(self, request):
        products = Product.objects.filter(product_status=0).order_by('-created_date')
            
        context = {
                'products': products,
            }
        return render(request, self.template_name, context)


class UsedProductsListView(View):
    """
    Class to display Only Used Products
    """
    model = Product()
    template_name = 'products/used_products.html'

    def get(self, request):
        products = Product.objects.filter(product_status=1).order_by('-created_date')
            
        context = {
                'products': products,
            }
        return render(request, self.template_name, context)


class ProductDetailsView(DetailView):
    """
    Class to display single Product
    """
    model = Product
    queryset = Product.objects.order_by('-created_date')
    template_name = 'products/product_details.html'
    fields = '__all__'
