"""Module for API views for `company` package."""

from typing import Any

from abstract_icd.views.base import ICDView
from companies.views.base import BaseCompanyView
from companies.serializers.input import CompanyToCreateRequest, CompanyToFetchRequest
from companies.serializers.output import CompanyResponse


class CompanyCreateView(ICDView, BaseCompanyView):
    """Handles request to the `company/<str:company_name>/` endpoint."""

    http_method_names = ['post']
    in_serializer_cls = CompanyToCreateRequest

    def process_request(self, request_params: Any) -> CompanyResponse:
        """
        process request for `company/<str:company_name>/` endpoint.

        :param request_params: Request parameters.
        :return: Serialized response.
        """
        response_data = self.service_class.create_company(**request_params)

        return CompanyResponse(response_data).data
