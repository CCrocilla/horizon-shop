from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator

from django.contrib.auth.forms import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Product
from .models import Category
from .models import SubCategory
from .models import ProductComment
from .models import ProductRating

from .forms import ProductCommentForm
from .forms import ProductRatingForm

from django.db.models import Q


def categories(request):
    return {
        'categories': Category.objects.all().filter(is_deleted=False)
    }


def subcategories(request):
    return {
        'subcategories': SubCategory.objects.all().filter(is_deleted=False)
    }


class AllProductsListView(View):
    """
    Class to display Users' Dashboard
    """
    model = Product()
    template_name = 'products/all-products.html'

    def get(self, request):
        products = Product.objects.order_by('-created_at'
                                            ).filter(is_deleted=False)
        search_term = None

        if 'sort' in request.GET:
            sort = request.GET['sort']
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort = f'-{sort}'
            products = products.order_by(sort)

        if 'q' in request.GET:
            search_term = request.GET['q']
            if not search_term:
                messages.error(
                    request, messages.ERROR, 'No Search createria entered!')
                return redirect(reverse('all_products'))

            searched = Q(title__icontains=search_term
                         ) | Q(
                             description__icontains=search_term
                               ) | Q(
                                   subcategory__name__icontains=search_term
                                     ) | Q(
                                         category__name__icontains=search_term
                                           ) | Q(
                                               brand__icontains=search_term
                                               )
            products = products.filter(
                searched, is_deleted=False).order_by('-created_at')

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
        products = Product.objects.filter(
            category=category, is_deleted=False)

        context = {
                'products': products,
                'category': category,
            }

        return render(request, self.template_name, context)


class SearchBySubCategoryView(View):
    model = Product()
    template_name = 'products/search_by.html'

    def get(self, request, slug_sub_cat):
        subcategory = get_object_or_404(SubCategory, slug=slug_sub_cat)
        products = Product.objects.filter(
            subcategory=subcategory, is_deleted=False)

        context = {
                'products': products,
                'subcategory': subcategory,
            }

        return render(request, self.template_name, context)


class NewProductsListView(View):
    """
    Class to display Only New Products
    """
    model = Product()
    template_name = 'products/new-products.html'
    paginate_by = 6

    def get(self, request):
        products = Product.objects.filter(
            product_status=0, is_deleted=False).order_by('-created_at')

        context = {
                'products': products,
            }
        return render(request, self.template_name, context)


class UsedProductsListView(View):
    """
    Class to display Only Used Products
    """
    model = Product()
    template_name = 'products/used-products.html'

    def get(self, request):
        products = Product.objects.filter(product_status=1, is_deleted=False
                                          ).order_by('-created_at')

        context = {
                'products': products,
            }
        return render(request, self.template_name, context)


class ProductDetailsView(View):
    """
    Class to display single Product Details on the Shop
    """
    template_name = 'products/product-details.html'

    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        comments = ProductComment.objects.filter(
            product=product).order_by('-commented_date')
        comments_form = ProductCommentForm(self.request.GET or None)
        rating_form = ProductRatingForm(self.request.GET or None)

        user_rated = None
        if request.user.is_authenticated:
            user_rated = ProductRating.objects.filter(
                rated_by=request.user, product=product)

        context = {
                'product': product,
                'comments': comments,
                'comments_form': comments_form,
                'rating_form': rating_form,
                'user_rated': user_rated,
            }
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        comments = ProductComment.objects.filter(product=product
                                                 ).order_by('-commented_date')
        rating_stars = ProductRating.objects.filter(product=product)
        comments_form = ProductCommentForm(request.POST)
        rating_form = ProductRatingForm(request.POST)

        if comments_form.is_valid():
            comment = comments_form.save(commit=False)
            comment.commented_by = request.user
            comment.product = product
            comment.save()

        if rating_form.is_valid():
            rating_stars = rating_form.save(commit=False)
            rating_stars.rated_by = request.user
            rating_stars.product = product
            rating_stars.save()

        return redirect(request.path)


def ProductCommentDeleteView(request, pk):
    """ Delete a product from the store """

    comment = get_object_or_404(ProductComment, id=pk)
    comment.delete()

    messages.success(
        request,
        'Comment deleted successfully!'
        )
    return redirect(reverse(
        'product_details',
        kwargs={'slug': comment.product.slug}))
