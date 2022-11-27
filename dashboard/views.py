from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404

from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.text import slugify

import string
from django.utils.crypto import get_random_string

from django.contrib.auth.forms import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from home.views import LoginRequired

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from products.models import Product
from products.models import Category
from products.models import SubCategory

from products_checkout.models import Order

from .models import ShippingAddress
from .models import Testimonial

from .forms import CustomerForm
from .forms import CustomerExtraForm
from .forms import ShippingAddressForm
from .forms import TestimonialForm
from .forms import ProductForm
from .forms import ProductAdminForm
from .forms import CategoryForm
from .forms import SubCategoryForm


class DashboardView(LoginRequired, View):
    """ Dashboard User """
    template_name = 'dashboard/dashboard.html'
    permission_denied_message = 'Authentication Error! Access reserved \
                                 only to Authenticated Customers!'

    def get(self, request):
        if request.user.is_superuser:
            orders = Order.objects.filter(billed=True).order_by('-created_at')

            products = Product.objects.all().count()

            addresses = ShippingAddress.objects.all().count()

            testimonials = Testimonial.objects.all().count()
        else:
            orders = Order.objects.filter(
                created_by=request.user, billed=True).order_by('-created_at')

            products = Product.objects.filter(
                created_by=request.user, is_deleted=False).count()

            addresses = ShippingAddress.objects.filter(
                created_by=request.user, is_deleted=False).count()

            testimonials = Testimonial.objects.filter(
                created_by=request.user).count()

        context = {
                'orders': orders,
                'products': products,
                'addresses': addresses,
                'testimonials': testimonials,
            }
        return render(request, self.template_name, context)


################################
#        Customer Views        #
################################
class CustomerView(LoginRequired, View):
    """
    Class to Edit Customer Information
    """
    model = User
    template_name = 'dashboard/customer/customer.html'

    def get(self, request):
        """ Function to retrive data for Booking """
        customer_form = CustomerForm(instance=request.user)
        customer_extra_form = CustomerExtraForm(instance=request.user.customer)

        context = {
            'customer_form': customer_form,
            'customer_extra_form': customer_extra_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ Post Function Booking """
        customer_form = CustomerForm(
            request.POST, instance=request.user
            )
        customer_extra_form = CustomerExtraForm(
            request.POST, request.FILES, instance=request.user.customer
            )

        if customer_form.is_valid():
            if customer_extra_form.is_valid():
                customer_form.save()
                customer_extra_form.save()

                messages.success(request, 'Profile Updated Correctly!')
                return HttpResponseRedirect(reverse('customer-update', ))
        else:
            messages.info(
                request,
                'Error: Form not filled in correctly! Please try again!'
                )
            return redirect(request.path)


class CustomerPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'dashboard/customer/customer-change-password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('change-password')
    success_message = "Hurray! Your password has been changed successfully!"


################################
#    Shipping Address Views    #
################################
class ShippingAddressAddView(SuccessMessageMixin, CreateView):
    """
    Class to create Users' Shipping Addresses
    """
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'dashboard/customer/shipping-address-add.html'
    success_url = reverse_lazy('shipping-address-list')
    success_message = 'Shipping Address was created successfully!'

    def get_initial(self):
        user = self.request.user
        return {'created_by': user}


class ShippingAddressListView(LoginRequired, ListView):
    """
    Class to display the User's Shipping Addresses
    """
    model = ShippingAddress
    template_name = 'dashboard/customer/shipping-address-list.html'
    ordering = ['-created_at']
    fields = '__all__'
    paginate_by = 6
    permission_denied_message = 'Authentication Error! Access reserved \
                                 only to Authenticated Customers!'

    def get_queryset(self):
        """
        Return a list of all the Shipping Address
        for the authenticated user.
        """
        queryset = ShippingAddress.objects.filter(
            created_by=self.request.user,
            is_deleted=False)
        return queryset


class ShippingAddressUpdateView(SuccessMessageMixin, UpdateView):
    """
    Class to update User's Testimonial
    """
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'dashboard/customer/shipping-address-update.html'
    success_url = reverse_lazy('shipping-address-list')
    success_message = "Shipping Address updated successfully!"


class ShippingAddressDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Testimonial
    """
    model = ShippingAddress
    template_name = 'dashboard/customer/shipping-address-delete.html'
    success_url = reverse_lazy('shipping-address-list')
    success_message = "Shipping Address deleted successfully!"


################################
#        Product Views         #
################################
def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug

    return unique_slug


class ProductAddView(SuccessMessageMixin, View):
    """
    Class to create Users' Product
    """
    model = Product
    template_name = 'dashboard/products/product-add.html'

    def get(self, request):
        product_form = None
        if request.user.is_superuser:
            product_form = ProductAdminForm(
                request.POST or None, request.FILES or None)
        else:
            product_form = ProductForm(
                request.POST or None, request.FILES or None)

        context = {
            'form': product_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        product_form = None
        if request.user.is_superuser:
            product_form = ProductAdminForm(
                request.POST or None, request.FILES or None)
        else:
            product_form = ProductForm(
                request.POST or None, request.FILES or None)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.created_by = request.user
            product.slug = slugify(product.title)

            while Product.objects.filter(slug=product.slug).exists():
                product.slug = product.slug + '-' + get_random_string(length=5)

            if product.created_by.is_superuser:
                product.product_status = request.POST.get('product_status')
            else:
                product.product_status = 1
            product.save()
            messages.success(
                request,
                'Thanks! Your Product has been created!'
                )
            return HttpResponseRedirect(reverse('products-list', ))
        else:
            messages.error(
                request,
                'Error: Form not filled in correctly! Try again!'
                )
            return redirect(request.path)


class ProductListView(LoginRequired, ListView):
    """
    Class to display the User's Product
    """
    model = Product
    template_name = 'dashboard/products/products-list.html'
    ordering = ['-created_at']
    fields = '__all__'
    paginate_by = 8
    permission_denied_message = 'Authentication Error! Access reserved \
                                 only to Authenticated Customers!'

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Product.objects.filter(is_deleted=False)
        else:
            queryset = Product.objects.filter(
                created_by=self.request.user,
                is_deleted=False)

        return queryset


class ProductsDeletedListView(LoginRequired, ListView):
    """
    Class to display the User's Deleted Product
    """
    model = Product
    template_name = 'dashboard/products/products-deleted-list.html'
    ordering = ['-created_at']
    fields = '__all__'
    permission_denied_message = 'Authentication Error! Access reserved \
                                 only to Admin Users!'

    def get_queryset(self):
        queryset = Product.objects.filter(is_deleted=True)

        return queryset


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    """
    Class to update User's Product
    """
    model = Product
    template_name = 'dashboard/products/product-update.html'
    success_url = reverse_lazy('products-list')
    success_message = "Product updated successfully!"

    def get_form_class(self):
        form_class = ProductAdminForm

        if self.request.user.is_superuser:
            form_class = ProductAdminForm
        else:
            form_class = ProductForm

        return form_class


def ProductDeleteView(request, slug):
    """ Soft Delete a product """
    if request.user.is_authenticated:
        product = get_object_or_404(Product, slug=slug)
        product.soft_delete()

        messages.success(
            request,
            f'Product {product.title} deleted successfully!'
            )
        return redirect(reverse('products-list'))
    return HttpResponseRedirect(reverse('products-list'))


def ProductRestoreView(request, slug):
    """ Restore a product """
    if request.user.is_authenticated:
        product = get_object_or_404(Product, slug=slug)
        product.restore()

        messages.success(
            request,
            f'Product { product.title } restored successfully!'
            )
        return redirect(reverse('products-list'))
    return HttpResponseRedirect(reverse('products-list'))


################################
#         Order Views          #
################################
class OrderListView(LoginRequired, ListView):
    """
    Class to display the User's Order
    """
    model = Order
    template_name = 'dashboard/products/order-list.html'
    ordering = ['-created_at']
    fields = '__all__'
    paginate_by = 6
    permission_denied_message = 'Authentication Error! Access reserved \
                                 only to Authenticated Customers!'

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Order.objects.filter(
                billed=True).order_by('-created_at')
        else:
            queryset = Order.objects.filter(
                created_by=self.request.user,
                billed=True).order_by('-created_at')

        return queryset


class OrderDetailsView(DetailView):
    """
    Class to display single User's Testimonial
    """
    model = Order
    queryset = Order.objects.order_by('-created_at')
    template_name = 'dashboard/products/order-details.html'
    fields = '__all__'


################################
#       Category Views         #
################################
class CategoryAddView(SuccessMessageMixin, CreateView):
    """
    Class to create Users' Category
    """
    model = Category
    template_name = 'dashboard/admin/category-add.html'

    def get(self, request):
        category_form = CategoryForm(request.POST or None)

        context = {
            'form': category_form,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        category_form = CategoryForm(request.POST)

        if category_form.is_valid():
            name = category_form.cleaned_data.get('name')
            if Category.objects.filter(name=name).exists():
                messages.error(request, 'Category already exists!')
                return redirect(request.path)
            else:
                category = category_form.save(commit=False)
                category.slug = slugify(category.name)
                category.save()
                messages.success(
                    request,
                    f'Thanks! Category { category.name } created!'
                    )
                return HttpResponseRedirect(reverse('category-list', ))
        else:
            messages.info(request,
                          'Error: Form not filled in correctly! Try again!'
                          )
            return redirect(request.path)


class CategoryListView(ListView):
    """
    Class to display the Categories
    """
    model = Category
    template_name = 'dashboard/admin/category-list.html'
    ordering = ['name']
    fields = ['name', ]
    paginate_by = 9

    def get_queryset(self):
        queryset = Category.objects.filter(is_deleted=False)

        return queryset


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    """
    Class to update Category
    """
    model = Category
    template_name = 'dashboard/admin/category-update.html'
    fields = ['name', ]
    success_url = reverse_lazy('category-list')
    success_message = "Category updated successfully!"


class CategoriesDeletedListView(ListView):
    """
    Class to display the Deleted Categories
    """
    model = Category
    template_name = 'dashboard/admin/deleted-category-list.html'
    ordering = ['name']
    fields = '__all__'

    def get_queryset(self):
        queryset = Category.objects.filter(is_deleted=True)

        return queryset


def CategoryDeleteView(request, pk):
    """ Soft Delete a Category from the store """
    if request.user.is_authenticated:
        category = get_object_or_404(Category, id=pk)
        category.soft_delete()

        messages.success(
            request,
            f'Category {category.name} deleted successfully!'
            )
        return redirect(reverse('category-list'))
    return HttpResponseRedirect(reverse('category-list'))


def CategoryRestoreView(request, pk):
    """ Restore a category from the Deleted Categories List """
    if request.user.is_authenticated:
        category = get_object_or_404(Category, id=pk)
        category.restore()

        messages.success(
            request,
            f'Category {category.name}  restored successfully!'
            )
        return redirect(reverse('category-list'))
    return HttpResponseRedirect(reverse('category-list'))


################################
#      Sub-Category Views      #
################################
class SubCategoryAddView(SuccessMessageMixin, CreateView):
    """
    Class to create Sub-Category
    """
    model = SubCategory
    template_name = 'dashboard/admin/sub-category-add.html'

    def get(self, request):
        subcategory_form = SubCategoryForm(request.POST or None)

        context = {
            'form': subcategory_form,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        subcategory_form = SubCategoryForm(request.POST)

        if subcategory_form.is_valid():
            name = subcategory_form.cleaned_data.get('name')
            if SubCategory.objects.filter(name=name).exists():
                messages.error(request, 'Sub-Category already exists!')
                return redirect(request.path)
            else:
                subcategory = subcategory_form.save(commit=False)
                subcategory.slug = slugify(subcategory.name)
                subcategory.save()
                messages.success(
                    request,
                    f'Thanks! Sub-Category { subcategory.name } created!'
                    )
                return HttpResponseRedirect(reverse('subcategory-list', ))
        else:
            messages.error(
                request,
                'Error: Form not filled in correctly! Try again!'
                )
            return redirect(request.path)


class SubCategoryListView(ListView):
    """
    Class to display the Sub-Categories
    """
    model = SubCategory
    template_name = 'dashboard/admin/sub-category-list.html'
    ordering = ['name']
    fields = ['category', 'name', ]
    paginate_by = 9

    def get_queryset(self):
        queryset = SubCategory.objects.filter(
            is_deleted=False).order_by('category')

        return queryset


class SubCategoryUpdateView(SuccessMessageMixin, UpdateView):
    """
    Class to update Sub-Category
    """
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'dashboard/admin/sub-category-update.html'
    success_url = reverse_lazy('subcategory-list')
    success_message = "Sub-Category updated successfully!"


class SubCategoriesDeletedListView(ListView):
    """
    Class to display the Deleted Categories
    """
    model = SubCategory
    template_name = 'dashboard/admin/deleted-subcategory-list.html'
    ordering = ['name']
    fields = '__all__'

    def get_queryset(self):
        queryset = SubCategory.objects.filter(is_deleted=True)

        return queryset


def SubCategoryDeleteView(request, pk):
    """ Soft Delete a Sub-Category from the store """
    if request.user.is_authenticated:
        subcategory = get_object_or_404(SubCategory, id=pk)
        subcategory.soft_delete()

        messages.success(
            request,
            f'Sub-Category {subcategory.name} deleted successfully!'
            )
        return redirect(reverse('subcategory-list'))
    return HttpResponseRedirect(reverse('subcategory-list'))


def SubCategoryRestoreView(request, pk):
    """ Restore a Sub-Category from the Deleted Sub-Categories List """
    if request.user.is_authenticated:
        subcategory = get_object_or_404(SubCategory, id=pk)
        subcategory.restore()

        messages.success(
            request,
            f'Sub-Category {subcategory.name}  restored successfully!'
            )
        return redirect(reverse('subcategory-list'))
    return HttpResponseRedirect(reverse('subcategory-list'))


################################
#       Testimonial Views      #
################################
class TestimonialAddView(SuccessMessageMixin, CreateView):
    """
    Class to create Users' Testimonial
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'dashboard/testimonials/testimonial-add.html'
    success_url = reverse_lazy('testimonials-list')
    success_message = "Testimonial was created successfully!"

    def get_initial(self):
        user = self.request.user
        return {'created_by': user}


class TestimonialListView(ListView):
    """
    Class to display the User's Testimonial
    """
    model = Testimonial
    template_name = 'dashboard/testimonials/testimonials-list.html'
    ordering = ['-created_at']
    fields = '__all__'
    paginate_by = 6

    def get_testimonial_auth_user(self):
        """
        Return a list of all the Testimonial
        for the authenticated user.
        """
        user = self.request.user
        return Testimonial.objects.filter(created_by=user)


class TestimonialDetailsView(DetailView):
    """
    Class to display single User's Testimonial
    """
    model = Testimonial
    queryset = Testimonial.objects.order_by('-created_at')
    template_name = 'dashboard/testimonials/testimonial-details.html'
    fields = '__all__'


class TestimonialUpdateView(SuccessMessageMixin, UpdateView):
    """
    Class to update User's Testimonial
    """
    model = Testimonial
    template_name = 'dashboard/testimonials/testimonial-update.html'
    fields = ['title', 'comment']
    success_url = reverse_lazy('testimonials-list')
    success_message = "Testimonial updated successfully!"


class TestimonialDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Testimonial
    """
    model = Testimonial
    template_name = 'dashboard/testimonials/testimonial-delete.html'
    success_url = reverse_lazy('testimonials-list')
    success_message = "Testimonial deleted successfully!"
