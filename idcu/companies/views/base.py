"""Base views for `company` view."""

from rest_framework.views import APIView
from companies.services import CompanyServices


class BaseCompanyView(APIView):
    """Base company view."""

    service_class = CompanyServices()
