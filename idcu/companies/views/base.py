"""Base views for `company` view."""

from rest_framework.views import APIView
from companies.services import CompanyServices
from companies.serializers.input import CompanyToCreateRequest


class BaseCompanyView(APIView):
    """Base company view."""

    service_class = CompanyServices()
    in_serializer_cls = CompanyToCreateRequest
