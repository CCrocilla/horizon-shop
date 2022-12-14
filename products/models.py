from django.db import models
from django.db.models import Avg

from django.shortcuts import reverse
from django.contrib.auth.models import User

from django_resized import ResizedImageField

from home.models import SoftDeleteModel


PRODUCT_STATUS = ((0, 'New'), (1, 'Used'))


class Category(SoftDeleteModel):
    name = models.CharField(
        max_length=254,
        null=False,
        blank=False
        )
    slug = models.SlugField(
        max_length=254,
        unique=True
        )

    class Meta:
        verbose_name_plural = 'Categories'
        """ Ordering by Name """
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('search_by', args=[self.slug])


class SubCategory(SoftDeleteModel):
    category = models.ForeignKey(
        Category,
        null=True,
        blank=False,
        on_delete=models.CASCADE
        )
    name = models.CharField(
        max_length=254
        )
    slug = models.SlugField(
        max_length=254,
        unique=True
        )

    class Meta:
        verbose_name_plural = 'Sub-Categories'
        """ Ordering by Name """
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('search_by_sub_cat', args=[self.slug])


class Product(SoftDeleteModel):
    category = models.ForeignKey(
        Category,
        null=True,
        blank=False,
        on_delete=models.SET_NULL
        )
    subcategory = models.ForeignKey(
        SubCategory,
        null=True,
        blank=False,
        on_delete=models.SET_NULL
        )
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )
    slug = models.SlugField(
        unique=True,
        max_length=254
        )
    title = models.CharField(
        max_length=254
        )
    description = models.TextField()
    brand = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
        )
    discounted_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
        )
    product_status = models.IntegerField(
        choices=PRODUCT_STATUS,
        default=0
        )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
        )
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        force_format="WEBP",
        upload_to='images/',
        quality=100,
        null=True,
        blank=True
        )

    class Meta:
        """ Sorting by Create Date """
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('product_details', args=[self.slug])

    def __str__(self):
        return self.title

    def get_avg_rating(self):
        rating = ProductRating.objects.filter(
            product=self).aggregate(rating_avg=Avg('rating_stars'))
        return (rating['rating_avg'])

    def get_count_rating(self):
        rating_count = ProductRating.objects.filter(product=self).count()
        return rating_count


class ProductComment(models.Model):
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    commented_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    commented_date = models.DateTimeField(
        auto_now_add=True
        )
    comment = models.TextField(
        null=False,
        blank=False
        )

    class Meta:
        """ Sorting by Create Date """
        ordering = ['-commented_date']

    def __str__(self):
        return self.comment


class ProductRating(models.Model):
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    rated_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    rating_stars = models.IntegerField(
        null=True,
        blank=False,
        )
