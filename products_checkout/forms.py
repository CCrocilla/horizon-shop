from django import forms
from django.forms import ModelForm
from .models import Order


class CheckoutForm(ModelForm):
    """ Form Checkout Page """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        self.fields['shipping_address'].widget.attrs['autofocus'] = True

    class Meta:
        model = Order

        fields = (
            'created_by',
            'shipping_address',
            'cart_products',
            )

        labels = {
            'created_by': 'Full Name',
            'shipping_address': 'Shipping Address',
            'cart_products': 'Products',
            }

        widgets = {
            'created_by': forms.HiddenInput(),
            'shipping_address': forms.HiddenInput(),
            'cart_products': forms.HiddenInput(),
            }
