from django import forms
from django.forms import ModelForm

from .models import ProductComment
from .models import ProductRating


class ProductCommentForm(ModelForm):
    """ Form Contact Us Page """
    def __init__(self, *args, **kwargs):
        super(ProductCommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False

    class Meta:
        model = ProductComment
        fields = (
            'comment',
            )

        labels = {
            'comment': 'Comment',
            }

        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-3',
                    'rows': 3,
                    'cols': 5,
                    'required': True}),
            }


class ProductRatingForm(ModelForm):
    """ Form for Testimonials """
    def __init__(self, *args, **kwargs):
        super(ProductRatingForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False

    class Meta:
        model = ProductRating

        fields = (
            'rating_stars',
            )

        labels = {
            'rating_stars': '',
            }

        widgets = {
            'rating_stars': forms.HiddenInput(),
            }
