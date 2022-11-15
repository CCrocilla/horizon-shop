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

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from products.models import Category
from products.models import SubCategory

from .models import ShippingAddress
from .models import Testimonial

from products.models import Product

from .forms import CustomerForm
from .forms import CustomerExtraForm
from .forms import ShippingAddressForm
from .forms import TestimonialForm
from .forms import ProductForm
from .forms import CategoryForm
from .forms import SubCategoryForm


class DashboardView(View):
    """ Dashboard User """
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        return render(request, self.template_name, {})


################################
#        Customer Views        #
################################
class CustomerView(LoginRequiredMixin, View):
    """
    Class to Edit Customer Information
    """
    model = User
    template_name = 'dashboard/customer/customer.html'

    def get(self, request):
        print("IN THE GET!!!")
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
        print("INSIDE THE POST!!!")
        customer_form = CustomerForm(
            request.POST, instance=request.user
            )
        customer_extra_form = CustomerExtraForm(
            request.POST, request.FILES, instance=request.user.customer
            )

        if customer_form.is_valid():
            print("I AM VALID: CUSTOMER_EXTRA")
            if customer_extra_form.is_valid():
                print("I AM VALID: CUSTOMER_FORM")
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


class ShippingAddressListView(ListView):
    """
    Class to display the User's Shipping Addresses
    """
    model = ShippingAddress
    template_name = 'dashboard/customer/shipping-address-list.html'
    ordering = ['-created_at']
    fields = '__all__'
    paginate_by = 6

    def get_queryset(self):
        """
        Return a list of all the Shipping Address
        for the authenticated user.
        """
        queryset = ShippingAddress.objects.filter(created_by=self.request.user)
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
        product_form = ProductForm(request.POST, request.FILES)

        context = {
            'form': product_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.created_by = request.user
            product.slug = slugify(product.title)

            while Product.objects.filter(slug=product.slug).exists():
                product.slug = product.slug + '-' + get_random_string(length=5)

            if product.created_by.is_superuser:
                product.product_status = 0
            else:
                product.product_status = 1
            product.save()
            messages.success(
                request,
                'Thanks! Your Product has been created!'
                )
            return HttpResponseRedirect(reverse('product-list', ))
        else:
            messages.error(
                request,
                'Error: Form not filled in correctly! Try again!'
                )
            return redirect(request.path)


class ProductListView(ListView):
    """
    Class to display the User's Product
    """
    model = Product
    template_name = 'dashboard/products/product-list.html'
    ordering = ['-created_at']
    fields = '__all__'

    def get_queryset(self):
        if self.request.user.is_superuser:
            # queryset = Product.objects.all()
            queryset = Product.objects.filter(is_deleted=False)
        else:
            queryset = Product.objects.filter(
                created_by=self.request.user,
                is_deleted=False)

        return queryset


class DeletedProductListView(ListView):
    """
    Class to display the User's Product
    """
    model = Product
    template_name = 'dashboard/products/product-list.html'
    ordering = ['-created_at']
    fields = '__all__'

    def get_queryset(self):
        queryset = Product.objects.filter(is_deleted=True)

        return queryset


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    """
    Class to update User's Product
    """
    model = Product
    form_class = ProductForm
    template_name = 'dashboard/products/product-update.html'
    success_url = reverse_lazy('product-list')
    success_message = "Product updated successfully!"


def ProductDeleteView(request, slug):
    """ Delete a product from the store """

    product = get_object_or_404(Product, slug=slug)
    product.soft_delete()

    messages.success(request, 'Product deleted successfully!')
    return redirect(reverse('product-list'))


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
                messages.success(request, 'Thanks! Category created!')
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


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    """
    Class to update Category
    """
    model = Category
    template_name = 'dashboard/admin/category-update.html'
    fields = ['name', ]
    success_url = reverse_lazy('category-list')
    success_message = "Category updated successfully!"


class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Category
    """
    model = Category
    template_name = 'dashboard/admin/category-delete.html'
    success_url = reverse_lazy('category-list')
    success_message = "Category deleted successfully!"


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
                messages.success(request, 'Thanks! Sub-Category created!')
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


class SubCategoryUpdateView(SuccessMessageMixin, UpdateView):
    """
    Class to update Sub-Category
    """
    model = SubCategory
    template_name = 'dashboard/admin/sub-category-update.html'
    fields = ['category', 'name', ]
    success_url = reverse_lazy('subcategory-list')
    success_message = "Sub-Category updated successfully!"


class SubCategoryDeleteView(SuccessMessageMixin, DeleteView):
    """
    Class to delete Sub-Category
    """
    model = SubCategory
    template_name = 'dashboard/admin/sub-category-delete.html'
    success_url = reverse_lazy('subcategory-list')
    success_message = "Category deleted successfully!"


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
