"""Module containing URL patterns for the `companies` app."""

from django.urls import path
from companies.views.company import CompanyCreateView, CompanyView

urlpatterns = [
    path('create-company', CompanyCreateView.as_view(), name='create-company'),
    path('get-company', CompanyView.as_view(), name='create-company'),
]
