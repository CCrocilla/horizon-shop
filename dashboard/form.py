""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Testimonial


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
                attrs={'class': 'form-control'}),
            'comment': forms.Textarea(
                attrs={'class': 'form-control'}),
            'rating_stars': forms.HiddenInput(),
        }
