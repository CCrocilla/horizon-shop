from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from products.models import Product
from dashboard.models import ShippingAddress


class ProductCart(models.Model):
    created_by = models.ForeignKey(User,
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE
                                   )
    created_at = models.DateTimeField(auto_now_add=True)
    billed = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        default=0
                                        )
    total = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                null=False,
                                blank=False,
                                editable=False
                                )

    class Meta:
        verbose_name_plural = 'Products Cart'

    def __str__(self):
        return self.name


class ProductCartItem(models.Model):
    product_cart = models.ForeignKey(ProductCart,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE
                                     )
    product = models.ForeignKey(Product,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE
                                )
    quantity = models.IntegerField(default=1,
                                   null=True,
                                   blank=True
                                   )
