# Generated by Django 4.1.2 on 2022-10-27 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Shipping Addresses'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='created_date',
            new_name='created_at',
        ),
    ]