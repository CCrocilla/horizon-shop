from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User

from products.models import Product


class CartProducts(models.Model):
    created_by = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    product = models.ForeignKey(
        Product,
        blank=False,
        null=False,
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Cart Products'

    def __str__(self):
        return self.product.title + ' ' + f'x{self.quantity}'

    def product_price(self):
        """
        Function that calculate the price of single products.
        """
        product_price = 0
        if self.product.discounted_price:
            product_price = self.product.discounted_price * self.quantity
        else:
            product_price = self.product.price * self.quantity
        return product_price
