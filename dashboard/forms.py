""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Customer
from .models import ShippingAddress
from .models import Testimonial

from products.models import Category
from products.models import SubCategory
from products.models import Product


class CustomerForm(ModelForm):
    """ Form for User's Information Edit Page """
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'date_joined',
                  'last_login',
                  )

        labels = {
            'username': 'Username *',
            'email': 'Email *',
            'first_name': 'First Name *',
            'last_name': 'Last Name *',
            'date_joined': 'Date Account Creation',
            'last_login': 'Last Login',
        }

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control border border-dark rounded-3'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control border border-dark rounded-3'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control border border-dark rounded-3'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control border border-dark rounded-3'}),
            'date_joined': forms.DateTimeInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'form-control border border-dark rounded-3',
                    }),
            'last_login': forms.DateTimeInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'form-control border border-dark rounded-3',
                    }),
        }


class CustomerExtraForm(ModelForm):
    """ Form for User's Extra Information Edit Page """
    class Meta:
        model = Customer
        fields = ['avatar']

        labels = {
            'avatar': 'Avatar',
        }

        widgets = {'avatar': forms.FileInput(
            attrs={
                'class': 'form-control form-control-file border rounded-3'
                }), }


class ShippingAddressForm(ModelForm):
    """ Form for Shipping Address """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        self.fields['shipping_name'].widget.attrs["autofocus"] = True
        self.fields['country'].required = True

    class Meta:
        model = ShippingAddress

        fields = (
            'created_by',
            'shipping_name',
            'country',
            'phone_number',
            'address_street',
            'apartment_number',
            'city',
            'postcode',
            )

        widgets = {
            'created_by': forms.HiddenInput(),
            'shipping_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control'}),
            'address_street': forms.TextInput(
                attrs={'class': 'form-control'}),
            'apartment_number': forms.TextInput(
                attrs={'class': 'form-control'}),
            'city': forms.TextInput(
                attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(
                attrs={'class': 'form-control'}),
        }


class ProductForm(ModelForm):
    """ Form for Products """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        self.fields['category'].widget.attrs['autofocus'] = True
        self.fields[
            'category'].queryset = Category.objects.filter(
                is_deleted=False)
        self.fields[
            'subcategory'].queryset = SubCategory.objects.filter(
                is_deleted=False)

    class Meta:
        model = Product

        fields = ('created_by',
                  'category',
                  'subcategory',
                  'title',
                  'description',
                  'brand',
                  'price',
                  'discounted_price',
                  'image'
                  )

        widgets = {
                'created_by': forms.HiddenInput(),
                'image': forms.FileInput(
                    attrs={'class': 'form-control-file'}),
        }


class ProductUpdateForm(ModelForm):
    """ Form for Products """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        self.fields['category'].widget.attrs['autofocus'] = True
        self.fields[
            'category'].queryset = Category.objects.filter(
                is_deleted=False)
        self.fields[
            'subcategory'].queryset = SubCategory.objects.filter(
                is_deleted=False)

    class Meta:
        model = Product

        fields = ('created_by',
                  'category',
                  'subcategory',
                  'title',
                  'description',
                  'brand',
                  'image'
                  )

        widgets = {
                'created_by': forms.HiddenInput(),
                'image': forms.FileInput(
                    attrs={'class': 'form-control-file'}),
        }


class ProductAdminForm(ModelForm):
    """ Form for Products """
    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        self.fields['category'].widget.attrs['autofocus'] = True
        self.fields[
            'category'].queryset = Category.objects.filter(
                is_deleted=False)
        self.fields[
            'subcategory'].queryset = SubCategory.objects.filter(
                is_deleted=False)

    class Meta:
        model = Product

        fields = ('created_by',
                  'category',
                  'subcategory',
                  'sku',
                  'title',
                  'description',
                  'brand',
                  'price',
                  'discounted_price',
                  'product_status',
                  'image'
                  )

        widgets = {
                'created_by': forms.HiddenInput(),
                'image': forms.FileInput(
                    attrs={'class': 'form-control-file'}),
        }


class ProductUpdateAdminForm(ModelForm):
    """ Form for Products """
    def __init__(self, *args, **kwargs):
        super(ProductUpdateAdminForm, self).__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        self.fields['category'].widget.attrs['autofocus'] = True
        self.fields[
            'category'].queryset = Category.objects.filter(
                is_deleted=False)
        self.fields[
            'subcategory'].queryset = SubCategory.objects.filter(
                is_deleted=False)

    class Meta:
        model = Product

        fields = ('created_by',
                  'category',
                  'subcategory',
                  'sku',
                  'title',
                  'description',
                  'brand',
                  'product_status',
                  'image'
                  )

        widgets = {
                'created_by': forms.HiddenInput(),
                'image': forms.FileInput(
                    attrs={'class': 'form-control-file'}),
        }


class CategoryForm(ModelForm):
    """ Form Category """
    class Meta:
        model = Category
        fields = ['name']

        labels = {
            'name': 'Category Name',
        }

        widgets = {
                'name': forms.TextInput(
                    attrs={'class': 'form-control'}),
        }


class SubCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubCategoryForm, self).__init__(*args, **kwargs)
        self.fields[
            'category'].queryset = Category.objects.filter(is_deleted=False)
        self.fields['category'].widget.attrs['autofocus'] = True

    """ Form Category """
    class Meta:
        model = SubCategory
        fields = ['category', 'name']

        labels = {
            'category': 'Select the Category',
            'name': 'Sub-Category Name',
        }

        widgets = {
                'name': forms.TextInput(
                    attrs={'class': 'form-control text-dark'}),
        }


class TestimonialForm(ModelForm):
    """ Form for Testimonials """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True

    class Meta:
        model = Testimonial

        fields = ('created_by',
                  'title',
                  'comment',
                  'rating_stars'
                  )

        labels = {
            'created_by': '',
            'title': 'Title',
            'comment': 'Comment',
            'rating_stars': '',
        }

        widgets = {
            'created_by': forms.HiddenInput(),
            'title': forms.TextInput(
                attrs={'class': 'form-control text-dark'}),
            'comment': forms.Textarea(
                attrs={'class': 'form-control text-dark'}),
            'rating_stars': forms.HiddenInput(),
        }
