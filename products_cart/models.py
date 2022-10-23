from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from products.models import Product


class ProductsCart(models.Model):
    product = models.ForeignKey(
        Product, blank=True, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products Cart'

    def __str__(self):
        return self.name
