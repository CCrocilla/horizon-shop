from django import forms
from django.forms import ModelForm
from products_checkout.models import Order


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
            )

        labels = {
            'created_by': 'Full Name',
            'shipping_address': 'Shipping Address',
            }

        widgets = {
            'created_by': forms.HiddenInput(),
            'shipping_address': forms.HiddenInput(),
            }
