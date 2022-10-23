from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Customer


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    """ Create the Customer Profile """
    if created:
        Customer.objects.create(customer=instance)


@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    """ Update the Customer Profile """
    instance.customer.save()
