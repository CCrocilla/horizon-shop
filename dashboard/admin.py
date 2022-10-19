from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """ Users' Testimonials """
    list_display = (
        'created_by', 'title', 'created_date', 'rating_stars')