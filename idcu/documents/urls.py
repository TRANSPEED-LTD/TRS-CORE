"""Module containing URL patterns for the `companies` app."""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from documents.views.documents import OrderCreateView

urlpatterns = [
    path('create-order', OrderCreateView.as_view(), name='create-order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
