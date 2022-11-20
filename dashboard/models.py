from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django_resized import ResizedImageField

from django_countries.fields import CountryField

from home.models import SoftDeleteModel


class Customer(models.Model):
    customer = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    customer_status = models.BooleanField(
        default=True,
        blank=True,
        null=True
        )
    avatar = ResizedImageField(
        default='default.jpg',
        size=[300, 300],
        crop=['middle', 'center'],
        upload_to='customer_avatar/',
        null=True,
        blank=True
        )

    def __str__(self):
        return self.customer.username


class ShippingAddress(SoftDeleteModel):
    created_by = models.ForeignKey(
        User,
        null=True, blank=True,
        on_delete=models.CASCADE,
        default=User
        )
    created_at = models.DateField(
        auto_now_add=True
        )
    shipping_name = models.CharField(
        max_length=100,
        blank=False,
        null=False
        )
    country = CountryField(
        blank_label='Country',
        null=True,
        blank=True
        )
    phone_number = models.CharField(
        max_length=20,
        blank=False,
        null=False
        )
    address_street = models.CharField(
        max_length=100,
        blank=False,
        null=False
        )
    apartment_number = models.CharField(
        max_length=100,
        blank=False,
        null=False
        )
    city = models.CharField(
        max_length=100,
        blank=False,
        null=False
        )
    postcode = models.CharField(
        max_length=20,
        blank=False,
        null=False
        )

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_at']
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
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    created_at = models.DateField(
        auto_now_add=True
        )
    title = models.CharField(
        max_length=100
        )
    comment = models.TextField(
        max_length=650,
        blank=False,
        null=False
        )
    rating_stars = models.IntegerField(
        null=True,
        blank=False
        )

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_at']

    def __str__(self):
        """ Return Title and Comment """
        return str(self.title)

    def get_absolute_url(self):
        """ Redirect to List of Testmonials """
        return reverse('testimonials-list')
