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
    product = models.ForeignKey(Product,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE
                                )
    quantity = models.IntegerField(default=1,
                                   null=True,
                                   blank=True
                                   )

    def get_product_price(self):
        final_price = 0
        if self.product.discounted_price:
            final_price = self.product.discounted_price * self.quantity
        else:
            final_price = self.product.price * self.quantity
        return final_price


class OrderCart(models.Model):
    order_cart_number: models.CharField(max_length=50,
                                        null=False, blank=True, editable=False
                                        )
    created_by = models.ForeignKey(User, null=True, blank=True,
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(ShippingAddress,
                                         on_delete=models.CASCADE)
    products_cart = models.ManyToManyField(ProductCart)
    billed = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, blank=False, editable=False
                                        )
    total_price = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, blank=False, editable=False
                                      )

    class Meta:
        verbose_name_plural = 'Products Cart'

    def __str__(self):
        return self.order_cart_number

    # Code Institute explaination auto creation unique order number.
    def _generate_order_cart_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_cart_number:
            self.order_cart_number = self._generate_order_cart_number()
        super().save(*args, **kwargs)