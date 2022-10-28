from django.db import models

from django.contrib.auth.models import User

from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True,
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wishlist'

    def __str__(self):
        return str(self.user)
