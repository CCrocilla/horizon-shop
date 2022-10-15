from django.db import models


class ContactUs(models.Model):
    """ Model for Users' Feedback """
    created_date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    comment = models.TextField(blank=False, null=False)
    terms = models.BooleanField(default=False, blank=False, null=False)

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']

    def __str__(self):
        """ Return Full Name """
        return str(self.full_name)