# Generated by Django 4.1.2 on 2022-11-02 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_checkout', '0004_alter_order_shipping_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_cost',
        ),
    ]
