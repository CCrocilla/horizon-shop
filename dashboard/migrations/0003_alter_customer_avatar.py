# Generated by Django 4.1.2 on 2022-11-05 02:39

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_address_street_1_shippingaddress_address_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='default.jpg', force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[300, 300], upload_to='customer_avatar/'),
        ),
    ]