from django import forms
from django.forms import ModelForm
from .models import ContactUs


class ContactUsForm(ModelForm):
    """ Form Contact Us Page """
    class Meta:
        model = ContactUs
        fields = ('full_name',
                  'email',
                  'comment',
                  'terms'
                  )

        labels = {
                    'full_name': 'Full Name',
                    'email': 'Email',
                    'comment': 'Message',
                    'terms': 'Terms & Conditions',
                }

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control text-dark rounded-3'
                    }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control text-dark rounded-3'
                    }),
            'comment': forms.Textarea(
                attrs={
                    'class':
                        'form-control text-dark rounded-3',
                        'rows': 3,
                        'cols': 5
                    }),
            'terms': forms.CheckboxInput(
                attrs={
                    'class': 'checkbox text-dark', 'required': ''
                    }),
            }
