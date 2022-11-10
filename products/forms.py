from django import forms
from django.forms import ModelForm

from .models import ProductComment
from .models import ProductRating


class ProductCommentForm(ModelForm):
    """ Form Contact Us Page """

    class Meta:
        model = ProductComment
        fields = (
            'comment',
            )

        labels = {
            'comment': '',
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
    """ Form for Product Rating """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rated_by'].disabled = True

    class Meta:
        model = ProductRating

        fields = (
            'rated_by',
            'rating_stars',
            )

        labels = {
            'rated_by': '',
            'rating_stars': '',
            }

        widgets = {
            'rated_by': forms.HiddenInput(),
            'rating_stars': forms.HiddenInput(),
            }
