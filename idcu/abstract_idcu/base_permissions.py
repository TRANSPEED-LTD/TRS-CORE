"""
This module defines base permission rules around all packages.

In our project, all view entries (which needs authentication)
should be checked, that request.user has an access to the company he's making request for.
"""

from rest_framework import permissions
from django.shortcuts import get_object_or_404
from companies.models import Company
from abstract_idcu.views.base import get_request_payload
from abstract_idcu.base_exceptions import PermissionNotPermitted


class HasSpecificCompanyPermission(permissions.BasePermission):
    """
    Custom permission to check if the user has permission to view a specific company.
    """

    def has_permission(self, request, view) -> bool:
        """
        Check if user has permission to get requested data.

        :param request: The DRF request.
        :param view: The DRF view.
        :return: True, if access permitted.

        :raises PermissionNotPermitted: If user has not access to requested company, or company's data.
        """
        vat_number = get_request_payload(request)["vat_number"]

        if vat_number is None:
            return False

        company = get_object_or_404(Company, vat_number=vat_number)

        if request.user.company != company:
            raise PermissionNotPermitted

        return True
