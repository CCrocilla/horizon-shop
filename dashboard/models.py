from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Customer(models.Model):
    customer = models.OneToOneField(
        User,
        null=True, blank=True,
        on_delete=models.CASCADE
        )
    customer_status = models.BooleanField(
        default=True,
        blank=True, null=True
        )
    avatar = models.ImageField(
        default='default.jpg',
        upload_to='customer_avatar/',
        null=True, blank=True
        )

    def __str__(self):
        return self.customer.username


class ShippingAddress(models.Model):
    created_by = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.CASCADE,
        default=User
        )
    created_date = models.DateField(
        auto_now_add=True
        )
    shipping_name = models.CharField(
        max_length=100,
        blank=False, null=False
        )
    country = CountryField(
        blank_label='Country',
        null=True, blank=True
        )
    phone_number = models.CharField(
        max_length=20,
        blank=False, null=False
        )
    address_street_1 = models.CharField(
        max_length=100,
        blank=False, null=False
        )
    address_street_2 = models.CharField(
        max_length=100,
        blank=False, null=False
        )
    city = models.CharField(
        max_length=100,
        blank=False, null=False
        )
    postcode = models.CharField(
        max_length=20,
        blank=False, null=False
        )

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return self.shipping_name

    def get_absolute_url(self):
        """ Redirect to List of Addresses of the User """
        return reverse('shipping-address-list')


class Testimonial(models.Model):
    """ Model Testimonial """
    created_by = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.CASCADE
        )
    created_date = models.DateField(
        auto_now_add=True
        )
    title = models.CharField(
        max_length=100
        )
    comment = models.TextField(
        max_length=650,
        blank=False, null=False
        )
    rating_stars = models.IntegerField(
        null=True, blank=False
        )

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']

    def __str__(self):
        """ Return Title and Comment """
        return str(self.title)

    def get_absolute_url(self):
        """ Redirect to List of Testmonials """
        return reverse('testimonials-list')
