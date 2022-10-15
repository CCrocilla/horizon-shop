from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """Contact Us"""
    list_display = (
        'full_name', 'email', 'comment', 'created_date', 'terms'
    )
