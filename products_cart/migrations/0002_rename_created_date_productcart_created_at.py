# Generated by Django 4.1.2 on 2022-10-27 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcart',
            old_name='created_date',
            new_name='created_at',
        ),
    ]
