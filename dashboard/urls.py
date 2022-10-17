from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import DashboardView


urlpatterns = [
    path(
        '', DashboardView.as_view(), name='dashboard'),
    # path(
    #     '', include('django.contrib.auth.urls')),
    ###########################################
    #            Testimonial Paths            #
    ###########################################
    # path(
    #     'testimonial/add',
    #     TestimonialAddView.as_view(),
    #     name='add-testimonial'
    #     ),
    # path(
    #     'testimonial/list',
    #     TestimonialListView.as_view(),
    #     name='list-testimonials'
    #     ),
    # path(
    #     'testimonial/<int:pk>/details',
    #     TestimonialDetailsView.as_view(),
    #     name='details-testimonial'
    #     ),
    # path(
    #     'testimonial/<int:pk>/edit',
    #     TestimonialUpdateView.as_view(),
    #     name='update-testimonial'
    #     ),
    # path(
    #     'testimonial/<int:pk>/delete',
    #     TestimonialDeleteView.as_view(),
    #     name='delete-testimonial'
    #     ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)