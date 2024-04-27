"""Module containing URL patterns for the `companies` app."""

from django.urls import path
from companies.views.company import CompanyCreateView

urlpatterns = [
    path('create_company', CompanyCreateView.as_view(), name='create_company'),
]
