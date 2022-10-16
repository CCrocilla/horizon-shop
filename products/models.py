from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Sub-Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(
        'SubCategory', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    description = models.TextField()
    brand = models.CharField(max_length=254, null=True, blank=True)
    item_weight = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    release_date = models.DateField()
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_status = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductComments(models.Model):
    product = models.ForeignKey(
        'Product', blank=True, null=True, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    commented_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    class Meta:
        """ Sorting by Create Date """
        ordering = ['commented_date']

    def __str__(self):
        return self.comment


class ProductRating(models.Model):
    product = models.ForeignKey(
        'Product', blank=True, null=True, on_delete=models.SET_NULL)
    rated_by = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    rating_stars = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
