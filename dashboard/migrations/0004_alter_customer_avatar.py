# Generated by Django 4.1.2 on 2022-11-24 02:22

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_customer_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[300, 300], upload_to='customer_avatar/'),
        ),
    ]
