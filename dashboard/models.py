from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Testimonial(models.Model):
    """ Model Testimonial """
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=650, blank=False, null=False)
    rating_stars = models.IntegerField(null=True, blank=False)

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']

    def __str__(self):
        """ Return Title and Comment """
        return str(self.title)

    def get_absolute_url(self):
        """ Redirect to List of Testmonials """
        return reverse('testimonial-list')
