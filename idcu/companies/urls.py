"""Module containing URL patterns for the `companies` app."""

from django.urls import path
from companies.views.company import (
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
    ForwarderCompanyView,
    CompaniesFilterView,
)

urlpatterns = [
    path('create-company', CompanyCreateView.as_view(), name='create-company'),
    path('update-company/', CompanyUpdateView.as_view(), name='update-company'),
    path('delete-company/', CompanyDeleteView.as_view(), name='delete-company'),
    path('get-user-company/', ForwarderCompanyView.as_view(), name='get-user-company'),
    path('get-companies/', CompaniesFilterView.as_view(), name='filter-companies')
]
