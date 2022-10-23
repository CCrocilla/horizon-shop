""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .models import Customer
from .models import ShippingAddress
from .models import Testimonial


class CustomerForm(ModelForm):
    """ Form for User's Information Edit Page """
    class Meta:
        model = User
        fields = ('username', 'email')

        labels = {
            'username': 'Username *',
            'email': 'Email *',
        }

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control'}),

            'email': forms.EmailInput(
                attrs={'class': 'form-control'}),
        }


class CustomerExtraForm(ModelForm):
    """ Form for User's Extra Information Edit Page """
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'avatar']

        labels = {
            'first_name': 'First Name *',
            'last_name': 'Last Name *',
            'avatar': 'Avatar',
        }

        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'avatar': forms.FileInput(
                    attrs={'class': 'form-control-file'}),
        }


class ShippingAddressForm(ModelForm):
    """ Form for Shipping Address """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        self.fields["shipping_name"].widget.attrs["autofocus"] = True

    class Meta:
        model = ShippingAddress

        fields = '__all__'

        widgets = {
            'created_by': forms.HiddenInput(),
            'shipping_name': forms.TextInput(
                    attrs={'class': 'form-control text-dark'}),
            'phone_number': forms.TextInput(
                    attrs={'class': 'form-control text-dark'}),
            'address_street_1': forms.TextInput(
                    attrs={'class': 'form-control text-dark'}),
            'address_street_2': forms.TextInput(
                    attrs={'class': 'form-control text-dark'}),
            'city': forms.TextInput(
                    attrs={'class': 'form-control text-dark'}),
            'postcode': forms.TextInput(
                    attrs={'class': 'form-control text-dark'}),
        }


class TestimonialForm(ModelForm):
    """ Form for Testimonials """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True

    class Meta:
        model = Testimonial

        fields = ('created_by', 'title', 'comment', 'rating_stars')

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