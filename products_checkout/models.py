import uuid

from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

from dashboard.models import ShippingAddress

from products_cart.models import CartProducts


class Order(models.Model):
    order_number = models.CharField(
        max_length=50,
        null=False,
        blank=True,
        editable=False
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
    shipping_address = models.ForeignKey(
        ShippingAddress,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    cart_products = models.ManyToManyField(
        CartProducts,
        )
    billed = models.BooleanField(
        default=False
        )
    delivered = models.BooleanField(
        default=False
        )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True, 
        editable=False
        )
    total_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
        )

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.order_number

    # Code Institute explaination auto creation unique order number.
    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def total_price(self):
        """
        Function to return the price of the Order.
        """
        order_total_price = 0
        for item in self.cart_products.all():
            order_total_price += item.product_price()
        return order_total_price

    def quantity_products(self):
        """
        Function to return the quantity of Products in the Order.
        """
        quantity = 0
        for item in self.cart_products.all():
            quantity += item.quantity
        return quantity
